from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseFlow(object):
    def __init__(self, name="None", describe="None"):
        """
        流程目的名字，以及相关描述
        :param name:      流程目的名字
        :param describe:  流程目的描述
        """
        pass

    def get_creator_id(self):
        """
        获取模板流程创建人id，类型输入只能为整型(interger)
        :return: 返回的数据类型为整型
        """
        pass

    def get_create_time(self):
        """
        获取模板流程创建时间，类型输入只能为(datetime)
        :return: 返回的数据类型为字符型
        """
        pass


class Step(object):
    """
    该有的条件类
    """

    def __init__(self):
        # 参数自定义
        pass

    def function(self):
        # 需要的方法自定义
        pass


class Action(object):
    def __init__(self, action_name=None, action_people=None, execute_action_time=None, start_action_time=None,
                 end_action_time=None, result_value=None, content=None):
        """

        :param action_name:         行为名字
        :param action_people:       行为执行人
        :param execute_action_time: 行为起始时间
        :param start_action_time:   行为执行时间
        :param end_action_time:     行为结束时间
        :param result_value:        行为是否完成（完成：1，未完成：0）
        :param content:
        """
        content = Content()
        content.get_html()            # 将Content类作为Action类的属性，继而可以使用Content中的属性和方法
        action_result = ActionResult(action_value='1243')
        action_result.action_value()   # 将Action_result类作为Action类的属性，继而可以使用ActionResult中的属性和方法

class ActionResult:
    def __init__(self, action_value=None):
        """
        行为结果，以及行为内容
        :param action_value: 行为结果
        :param content:      行为内容
        """
        pass

    def action_value(self):
        """
        获取行为结果（0为False，1为True）
        :return:
        """
        pass


class Content():
    def get_html(self):
        html_data = '结果有误'  # 获取用户返回的行为内容


class UseFlow(BaseFlow):
    """
    继承BaseFlow，拥有BaseFlow的属性和方法，如果需要自定义请覆盖
    """
    pass


class UseStep(Step):
    """
    继承Step，拥有Step的属性和方法，如果需要自定义请覆盖
    """
    pass


class UseAction(Action):
    """
    继承Action，拥有Action的属性和方法，如果需要自定义请覆盖
    """
    pass


class Login(object):
    """
    登录功能
    """

    def login(self):
        """"
        前台获取用户登录信息，根据用户账号、密码校验是否是系统用户以及密码是否匹配正确
        """
        username = '马云的小妹'  # 卡安泰获取数据，数据代替
        password = '123'
        status = True
        return {"status": status, "msg": '登录成功', "code": 200}


class Register(object):
    """
    注册功能
    """

    def register(self):
        """
        获取用户在注册界面上输入的注册信息，进行表单数据的格式校验(手机号是否满足11位等)，然后将数据写入用户表中
        :return:
        """
        username = '马云的小妹'  # 前台用户注册数据提交，获取的用户账号
        password = '123'
        name = 'mama'
        moblie_phone = '15095356694'
        outlook = 'it-22'
        status = True
        return {"status": status, "msg": '注册成功', "code": 200}


class WorkflowDefinition(object):
    """
    流程定义
    """

    def workflow_definition(self):
        """
        获取到前台界面中用户创建的流程的所有节点信息的json数据，拆分json数据为数据库设计的字段信息，并把数据写入数据表中
        :return:
        """
        workflow_json = {'flow_name':'未消出货订单','flow_desc':'当有新的未消出货订单产生时','flow': {'flow_tilt': '付款流程', 'flow_desc': '完成财务付款的流程'},
                         'step_list': [{'execution_time': '2021-8-25 08：30：00', 'last_execution_time': '',
                                        'next_execution_time': '', 'execution_step': '一段sql语句'}],
                         'action_list': [{'动作排序号': 1, '动作标题': '查询未消出货订单'}],
                         'action_result': [{'行为结果': '满足', '关联的行为id': 1}]}
        # 根据workflow_json获取数据表中的对应字段数据，并将写入数据表中
        flow_name = workflow_json['flow_name']
        flow_desc = workflow_json['flow_desc']
        flow = workflow_json['flow']
        step_list = workflow_json['step_list ']
        action_list = workflow_json['action_list ']
        action_result_list = workflow_json['action_result  ']
        create_time = '2021-08-25 09:19:00'
        try:
            db.session.execute(f"""
                            insert into TempFlow(tflow_name,tflow_desc,flow,step_list,action_list,action_result_list,creator,create_time)
                            values('{flow_name}','{flow_desc}','{flow}','{step_list}','{action_list}','{action_result_list}','{create_time}')
                        """)
            result = {'status':True,'msg':'新增模板流程数据成功','code':200}
        except Exception as e:
            print("写入模板流程中的数据回滚!", e)
            db.session.rollback()
            result = {'status':False,'msg':'新增模板流程数据失败','code':400}
        db.session.commit()
        return result


class UpdateTempFlow(object):
    """
    修改模板流程
    """

    def update_tempflow(self):
        """
        修改模板流程
        具体代码流程：先获取当前用户需要修改的模板流程(调用查询模板流程方法)，然后从前台获取用户修改好的模板流程数据，再写入数据库模板流程表中
        :return:
        """
        pass

class UpdateUseFlow(object):
    """
    修改用户使用流程
    """

    def update_userflow(self):
        """
        修改用户使用流程
        具体代码流程：先获取当前用户需要修改的用户流程(调用查询当前用户使用过的流程方法)，然后从前台获取用户修改好当前操作流程数据，再写入数据库流程表、条件表、行为表、行为结果表中
        :return:
        """
        pass


class UseWorkflow(object):
    """
    流程使用类
    """

    def use_workflow(self):
        """
        新增用户使用流程
        具体代码流程：先获取当前用户需要操作的模板流程(调用查询模板流程方法)，然后从前台获取用户添加好的模板流程数据，再写入数据库流程表、条件表、行为表、行为结果表中
        :return:
        """
        pass


class DeleteTempFlow(object):
    """
    删除模块流程（逻辑删）
    """

    def delete_tempflow(self):
        """
        删除模板流程，即把模板流程中的is_deleted从0变成1
        :return:
        """
        pass

class DeleteUseFlow(object):
    """
    删除用户操作流程（逻辑删）
    """

    def delete_tempflow(self):
        """
        删除当前用户操作过的流程，即把模板流程中的is_deleted从0变成1(与当前用户关联)
        :return:
        """
        pass

class SearchTempFlow(object):
    """
    查询流程模块
    """

    def search_tempflow(self):
        """
        根据用户在前台界面上选择点击的流程，能够获取到流程标题查询模板流程所有节点信息
        :return:
        """
        pass

class SearchUseFlow(object):
    """
    查询当前用户操作过的所有流程
    """

    def search_userflow(self):
        """
        获取当前操作用户的信息获取到用户id，对应流程表中的creator，即可以查询到用户操作的流程
        :return:
        """
        db


class ExecuteFlow(object):
    """
    执行流程类
    """

    def execute_flow(self):
        """
        根据流程中的条件判断是否触发，再根据流程中的行为来执行具体的行为动作
        :return:
        """
        pass
