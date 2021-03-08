def window_to_viewPort_transformation_x(x_w, w_width, vp_width):
	x_vp = ((x_w - 0) / (w_width)) * vp_width
	return x_vp
	print('X VP:', x_vp)

def window_to_viewPort_transformation_y(y_w, w_height, vp_height):
	y_vp = (1-((y_w - 0)/w_height)) * vp_height
	print('y VP:', y_vp)
	return(y_vp)

def window_to_viewPort(x_w, y_w, w_width, w_height, vp_width, vp_height):
	x_vp = window_to_viewPort_transformation_x(x_w, w_width, vp_width)
	y_vp = window_to_viewPort_transformation_y(y_w, w_height, vp_height)
	return(x_vp, y_vp)