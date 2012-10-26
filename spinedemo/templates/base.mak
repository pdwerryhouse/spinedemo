<!DOCTYPE html>
<html>
<head>
  <title>Spinedemo</title>
  <link rel="stylesheet" href="${request.static_url('spinedemo:static/css/spinedemo.css')}" type="text/css" charset="utf-8">

  <script src="${request.static_url('spinedemo:static/js/json2.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/jquery.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/jquery.tmpl.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/spine.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/spine.local.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/spine.relation.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/spine.ajax.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/js/spine.route.js')}" type="text/javascript" charset="utf-8"></script>

  <script src="${request.static_url('spinedemo:static/app/country.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/app/person.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('spinedemo:static/app/router.js')}" type="text/javascript" charset="utf-8"></script>
</head>
<body>
  
	${self.body()}

</body>
</html>
