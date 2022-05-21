class Device():
	def __init__(self,params,config,mock=False):
		self.config = config
		self.params = params
		# self.flow_dev_lim = 2
		# self.emergency_flows = {}
		self.subdevices = {}

		if mock:
			self.ser = None
			for subdev_name in params.keys(): #for each subdevice in input file
				self.subdevices[subdev_name] = Mock_Subdevice(subdev_name,params[subdev_name],config["Subdevices"][subdev_name])

	def get_pv(self,subdev_name):
		return self.subdevices[subdev_name].get_pv()

	def get_sp(self,subdev_name):
		return self.subdevices[subdev_name].get_sp()

	def set_sp(self,subdev_name,sp_value):
		return self.subdevices[subdev_name].set_sp(sp_value)

	def is_emergency(self,subdev_name,pv_read_time,sp_set_time,current_sp,current_pv):
		return self.subdevices[subdev_name].is_emergency(pv_read_time,sp_set_time,current_sp,current_pv)

	def get_subdevice_names(self):
		return self.subdevices.keys()

	def get_emergency_sp(self,subdev_name):
		return self.subdevices[subdev_name].emergency_setting


class Mock_Subdevice():
	def __init__(self,name,params,config):
		self.name = name
		self.units = params["Units"]
		self.emergency_setting = params["Emergency Setpoint"]
		self.current_sp = None

	def is_emergency(self,pv_read_time,sp_set_time,current_sp,current_pv):
		return [False,self.name,current_sp,current_pv]
	def get_pv(self):
		return self.current_sp
	def set_sp(self,sp_value):
		self.current_sp = sp_value
		return True

	def get_sp(self):
		return self.current_sp