
var Country = Spine.Model.sub();

Country.configure("Country", "name");
Country.hasMany("persons", "Person");

Country.extend(Spine.Model.Ajax);

Country.extend({
    url: "/api/countries"
});

var CountryApp = Spine.Controller.sub({
  elements: {
    ".items": "items"
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

