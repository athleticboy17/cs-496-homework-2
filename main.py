import webapp2

# Arbitary name of 'base-data'
config = {'default-group':'base-data'}

application = webapp2.WSGIApplication([
	('/edit/channel', 'edit_channel.EditChannel'),
	('/edit', 'edit.Edit'),
	('/view/channel', 'view_channel.ViewChannel'),
	('/view', 'view.View'),
	('/channel/add', 'add_channel.AddChannel'),
	('/', 'admin.Admin'),
	('/base', 'base_page.HelloWorld'),
], debug=True, config=config)