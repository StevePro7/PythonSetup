SQL Alchemy 03
18-Aug-2024


Mixin and Custom Base Classes
https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html

When using declarative to share functionality e.g. set of common columns

@declarative_mixin
"mixin" class which is inherited from in addition to the primary base