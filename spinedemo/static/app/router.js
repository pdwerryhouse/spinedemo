
jQuery(function($) {
  // Temporary kludge to get rid of the countries form.
  // This will go when I figure out how to display only one form at
  // a time.

  $("#countries").text("");
  return new PersonApp({
    el: $("#persons")
  });
});

