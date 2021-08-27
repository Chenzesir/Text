# import os
# from flask import Flask,url_for,request,render_template,Response,make_response
#
# # app = Flask(__name__)
# app=Flask(__name__,template_folder='templates',static_url_path='/static/')
# # @app.route('/<name>',endpoint='name')
# @app.route('/<int:url>',endpoint='name')
# def first_flask(url):
#     dir = request.full_path
#     # dir = os.path.join(request.host_url,url_for('name',url=url))
#     print(request.full_path)
#     # print(dir)
#     # return render_template('login.html',**{'dir':dir})
#     # return Response(dir,mimetype='application/json;charset=utf-8')
#     response = make_response(render_template('login.html'))
#
#     # response是flask.wrappers.Response类型
#
#     # response.delete_cookie('key')
#
#     response.set_cookie('url', dir)
#
#     response.headers['X-Something'] = 'A value'
#
#     return response
# # @app.route('/<path:url>',endpoint='name1')
# # def first_flask(url):
# #     print(url_for('name1',url=url)) #如果设置了url参数，url_for（别名,加参数）
# #     return 'Hello World'
#
# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets
# from redis import Redis
app = Flask(__name__, template_folder='templates')
app.debug = True



class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='张根'                                             #设置input标签中默认值
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(                                #第二次输入密码
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")  #验证2次输入的密码是否一致？
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),    #生成email input标签
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(                                        #choice radio选项
            (1, '男'),
            (2, '女'),
        ),
        coerce=int                                       #讲用户提交过来的 '4' 强制转成 int 4
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(                      #select 下拉框多选框
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),        #生成Checkbox 多选框
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):                        #重写form验证类的__init__方法可以实时同步数据中数据
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))


    def validate_pwd_confirm(self, field):                       #wtforms验证 钩子函数
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field:确认密码字段（应该是固定传参值）
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证

class register:
    @app.route('/register/', methods=['GET', 'POST'])
    def register(self):
        if request.method == 'GET':
            form = RegisterForm(data={'gender': 1})  #默认值
            return render_template('register.html', form=form)
        else:
            form = RegisterForm(formdata=request.form)
            if form.validate():
                print('用户提交数据通过格式验证，提交的值为：', form.data)
            else:
                print(form.errors)
            return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run()





