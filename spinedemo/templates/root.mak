<%inherit file="base.mak"/>

<script type="text/x-jquery-tmpl" id="personListTemplate">
	<p>HELLO</p>
</script>

<script type="text/x-jquery-tmpl" id="countryOption">
      <option value="${"${id}" | n}">${"${name}" | n}</option>
</script>

<script type="text/x-jquery-tmpl" id="countryTemplate">
  <div class="item">
    <div class="view">
      <span>${"${name}" | n}</span>
    </div>
  </div>
</script>

<script type="text/x-jquery-tmpl" id="personTemplate">
  <div class="item">
    <div class="view">
      <span>${"${firstname}" | n}</span>
      <span>${"${surname}" | n}</span>
    </div>
  </div>
</script>

<div id="views">

	<div id="view">
	</div>

	<div id="countries">
		<div class="items"></div>
		<form id="countryform">
			<input id="name" name="name" type="text" placeholder="Country Name..."></input>
			<input type="submit"/>
		</form>
	</div>

	<div id="persons">
		<div class="items"></div>
		<form id="personform">
			<input id="firstname" name="firstname" type="text" placeholder="First Name..."></input>
			<input id="surname" name="surname" type="text" placeholder="Surname..."></input>
			<select id="country_id" name="country_id">
			</select>
			<input type="submit"/>
		</form>
	</div>

</div>

