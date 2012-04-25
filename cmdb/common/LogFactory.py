# -*- coding:utf-8 -*-
import logging
import traceback

class LogFactory(object):
	def __init__(self,className):
		self.logger = logging.getLogger(className)

	def error(self,expectValue = None, actualValue = None, errorMsg = None):
		"""
		异常格式：期望出现{expectValue}，实际出现{actualValue}，异常信息{errorMsg}，系统异常信息{traceback}
		"""
		msg = u'[ERROR]异常日志：期望出现值 %s , 实际出现值 %s , 异常信息 %s' %(expectValue,actualValue,errorMsg)
		self.logger.error(msg.encode('utf-8'))
		exceptionMsg = traceback.format_exc()
		if exceptionMsg:
			self.logger.error(exceptionMsg)

	def info(self,infoMsg):
		"""
		信息格式：{infoMsg}
		"""
		msg = u'[INFO]信息日志：%s' %infoMsg
		self.logger.info(msg.encode('utf-8'))

	def debug(self,debugMsg = None,**argValue):
		"""
		Debug信息格式：Debug参数 = {argValue} , 信息 = {debugMsg}
		"""
		argMsg = ''
		for key in argValue:
			argMsg +=  "%s : %s " % (key,argValue[key])

		msg = u'[DEBUG]调试日志： Debug参数 %s , 信息 = %s'%(argMsg,debugMsg)
		self.logger.debug(msg.encode('utf-8'))
		