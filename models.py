class Category(models.Model):
    """
    actually our wiki, containing concepts and tags, linked to by markdown
    """
    category = models.CharField(max_length=64, primary_key=True)        # Local Authority, Planning Authority, etc
    text = models.TextField()


class Organisation(models.Model):
    organisation = models.CharField(max_length=64, primary_key=True)    # government-organisation:D6
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    area = models.ForeignKey(Area)
    text = models.TextField()


class Licence(models.Model):
    licence = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=256)
    text = models.TextField()


class Attribution(models.Model):
    attribution = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=256)


class Publication(models.Model):
    """
    documents published by an organisation
    """
    publication = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=256)
    organisation = models.ForeignKey(Organisation)
    licence = models.ForeignKey(Licence)
    attribution = models.ForeignKey(Attribution)
    category = models.ForeignKey(Category)
    url = models.URLField() 
    data_url = models.URLField()
    # task = models.ForeignKey(Task) # how to fetch an edition ..


class Edition(models.Model):
    """
    instance of a publication 
    """
    publication = models.ForeignKey(Publication)
    collected = models.DateTimeField() 


class Dataset(models.Model):
    """
    a register or pseudo register built from a publication for our domain .. 
    """
    dataset = models.CharField(max_length=64, primary_key=True)


class Datatype(models.Model):
    datatype = models.CharField(max_length=64, primary_key=True)
    text = models.TextField()


class Field(models.Model):
    field = models.CharField(max_length=64, primary_key=True)
    text = models.TextField()
    datatype = models.ForeignKey(Datatype)


class Value(models.Model):
    field = models.ForeignKey(Field)
    value = models.TextField()          # contents depending on datatype


class Item(models.Model):
    dataset = models.ForeignKey(Dataset)
    values = models.ManyToMany(Value)
