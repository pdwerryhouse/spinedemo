
var Country = Spine.Model.sub();

Country.configure("Country", "name");
Country.hasMany("persons", "Person");

Country.extend(Spine.Model.Ajax);

Country.extend({
    url: "/api/countries"
});

var CountryApp = Spine.Controller.sub({
  events: {
    "submit form": "create",
    "click .clear": "clear"
  },

  elements: {
    ".items": "items",
    "#countryform #name": "name"
  },

  init: function(){
    Country.bind("create",  this.proxy(this.addOne));
    Country.bind("refresh", this.proxy(this.addAll));
    Country.fetch();
  },

  addOne: function(country){
    var view = new Countries({item: country});
    this.items.append(view.render().el);
  },

  addAll: function(){
    Country.each(this.proxy(this.addOne));
  },

  create: function(e) {
    e.preventDefault();
    Country.create({
        name: this.name.val()
    });
    this.name.val("");
  },

  clear: function() {
    Country.destroyDone();
  }
});

var Countries = Spine.Controller.sub({      
  init: function(){
    this.item.bind("update", this.proxy(this.render));
    this.item.bind("destroy", this.proxy(this.remove));
  },

  render: function(){
    this.replace($("#countryTemplate").tmpl(this.item));
    return this;
  },

  remove: function(){
    this.el.remove();
    this.release();
  }
});

