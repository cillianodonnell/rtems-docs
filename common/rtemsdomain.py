from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType, Index
from sphinx.util.compat import Directive
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, TypedField

"""
:r:bsp:`sparc/sis`

:r:arch:`sparc`

:r:board:`...`

:r:user:`amar`

:r:list:`devel`
"""

role_name = {
	"bsp":		"BSP",
	"arch":		"Architecture",
	"board":	"Board",
	"user":		"User",
	"list":		"Mailing List",
	"rtems":	"`RTEMS`",
}

role_url = {
	"trac": 			("Trac",				"https://devel.rtems.org"),
	"devel": 			("Developer Site",		"https://devel.rtems.org"),
	"www":				("RTEMS Home",			"https://www.rtems.org/"),
	"buildbot":			("Buildbot Instance",	"https://buildbot.rtems.org/"),
	"builder":			("Builder Site",		"https://builder.rtems.org/"),
	"docs":				("Documentation Site",	"https://docs.rtems.org/"),
	"lists":			("Mailing Lists",		"https://lists.rtems.org/"),
	"git":				("Git Repositories",	"https://git.rtems.org/"),
	"ftp":				("FTP File Server",	"https://ftp.rtems.org/"),
	"review":			("Gerrit Code Review",	"https://review.rtems.org/"),
	"bugs":				("Bugs Database",		"https://devel.rtems.org/wiki/Bugs/"),
	"gsoc":				("Google Summer of Code", "https://devel.rtems.org/wiki/GSoC/"),
	"socis":			("ESA SOCIS",			"https://devel.rtems.org/wiki/SOCIS/")
}


role_list = {
	"announce":	("Announce Mailing List",			"https://lists.rtems.org/mailman/listinfo/announce/"),
	"bugs":		("Bugs Mailing List",				"https://lists.rtems.org/mailman/listinfo/bugs/"),
	"devel":	("Developers Mailing List",			"https://lists.rtems.org/mailman/listinfo/devel/"),
	"build":	("Build logs",						"https://lists.rtems.org/mailman/listinfo/build"),
	"users":	("Users Mailing List",				"https://lists.rtems.org/mailman/listinfo/users/"),
	"vc":		("Version Control Mailing List",	"https://lists.rtems.org/mailman/listinfo/vc/"),
}


def rtems_resolve_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
	role = name.split(":")[1] #XXX: is there a better way?

	try:
		if role == "list":
			text, url = role_list[text]
		elif role == "url":
			text, url = role_url[text]
	except KeyError:
		msg = inliner.reporter.error("rtems_resolve_role: '%s' is not a valid %s" % (text, role))
		err = inliner.problematic("ERROR: %s" % rawtext, None, msg)
		return [err], [msg]

	# XXX: how do you add an alt tag?
	node = nodes.reference(rawtext, text, refuri=url, **options)
	return [node], []



class RTEMSXrefRole(XRefRole):
	def __init__(self, item, title, **kwargs):
		XRefRole.__init__(self, **kwargs)
		self.item = item
		self.title = title

	def process_link(self, env, refnode, has_explicit_title, title, target):
		if has_explicit_title:
			title = has_explicit_title

		return has_explicit_title or self.title, target




class RTEMSDomain(Domain):
	"""RTEMS domain."""

	name = "r"
	label = "RTEMS"

	directives = {}
	object_types = {}

	roles = {
		"bsp":		RTEMSXrefRole("bsp", "BSP"),
		"arch":		RTEMSXrefRole("arch", "Architecture"),
		"user":		RTEMSXrefRole("user", "User"),
		"list":		rtems_resolve_role,
		"url":		rtems_resolve_role,
	}


	def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
		info = "*info*"
		anchor = "*anchor*"
		title = "*title*"

		return make_refnode(builder, fromdocname, info, anchor, contnode, title)

	def merge_domaindata(self, docnames, otherdata):
		pass # XXX is this needed?



def setup(app):
	app.add_domain(RTEMSDomain)
	return {'version': "1.0", 'parallel_read_safe': True}
