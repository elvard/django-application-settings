from django.conf import settings

def metasyntactic_variables(request):
	"""Include the meta-syntactic variables"""
	r = {}
	
	for var in settings.FOO_VARIABLES:
		r[var] = getattr(settings, 'FOO_%s' % var)
	return r