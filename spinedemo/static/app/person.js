
var Person = Spine.Model.sub();

Person.configure("Person", "firstname", "surname");
Person.belongsTo('country', 'Country');

Person.extend(Spine.Model.Ajax);

Person.extend({
    url: "/api/persons"
});

var PersonApp = Spine.Controller.sub({ 
  events: {
    "submit form": "create",
    "click .clear": "clear"
  },

  elements: {
    ".items": "items",
    "form #firstname": "firstname",
    "form #surname": "surname",
    "form #country_id": "country_id"
  },

  init: function(){
    Person.bind("create",  this.proxy(this.addOne));
    Person.bind("refresh", this.proxy(this.addAll));
    Person.fetch();
    Country.fetch();
  },

  addOne: function(person){
    var view = new Persons({item: person});
    this.items.append(view.render().el);
  },

  addAll: function(){
    Person.each(this.proxy(this.addOne));
  },

  create: function(e) {
    e.preventDefault();
    Person.create({
            firstname: this.firstname.val(), 
            surname: this.surname.val(),
            country_id: this.country_id.val(),
    });
    this.firstname.val("");
    this.surname.val("");
  },

  clear: function() {
   Person.destroyDone();
  }
});

var Persons = Spine.Controller.sub({      
  init: function(){
    this.item.bind("update", this.proxy(this.render));
    this.item.bind("destroy", this.proxy(this.remove));
  },

  render: function(){
    this.replace($("#personTemplate").tmpl(this.item));
    return this;
  },

  remove: function(){
    this.el.remove();
    this.release();
  }
});

