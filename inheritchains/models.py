from django.db import models
from deep.models import Level1, Level2, Level3, Level4

class Mixin1(models.Model):
    name1 = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Mixin2(models.Model):
    name2 = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Mixin3(models.Model):
    name3 = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Mixin4(models.Model):
    name4 = models.CharField(max_length=255)

    class Meta:
        abstract = True



class Leaf1(Mixin1, Mixin2, Mixin3, Mixin4):
    leaf_name = models.CharField(max_length=255)
    level1 =  models.ForeignKey(Level1)
    level2 =  models.ForeignKey(Level2)
    level3 =  models.ForeignKey(Level3)
    level4 =  models.ForeignKey(Level4)


class Leaf11(Leaf1):
    sub_leaf_name = models.CharField(max_length=255)
    sub_level1 =  models.ForeignKey(Level1)
    sub_level2 =  models.ForeignKey(Level2)
    sub_level3 =  models.ForeignKey(Level3)
    sub_level4 =  models.ForeignKey(Level4)


class Leaf12(Leaf1):
    sub_leaf_name = models.CharField(max_length=255)
    sub_level1 =  models.ForeignKey(Level1)
    sub_level2 =  models.ForeignKey(Level2)
    sub_level3 =  models.ForeignKey(Level3)
    sub_level4 =  models.ForeignKey(Level4)


class Leaf2(Mixin1, Mixin2, Mixin3, Mixin4):
    leaf_name = models.CharField(max_length=255)
    level1 =  models.ForeignKey(Level1)
    level2 =  models.ForeignKey(Level2)
    level3 =  models.ForeignKey(Level3)
    level4 =  models.ForeignKey(Level4)


class Leaf21(Leaf2):
    sub_leaf_name = models.CharField(max_length=255)
    sub_level1 =  models.ForeignKey(Level1)
    sub_level2 =  models.ForeignKey(Level2)
    sub_level3 =  models.ForeignKey(Level3)
    sub_level4 =  models.ForeignKey(Level4)

class Leaf22(Leaf2):
    sub_leaf_name = models.CharField(max_length=255)
    sub_level1 =  models.ForeignKey(Level1)
    sub_level2 =  models.ForeignKey(Level2)
    sub_level3 =  models.ForeignKey(Level3)
    sub_level4 =  models.ForeignKey(Level4)



