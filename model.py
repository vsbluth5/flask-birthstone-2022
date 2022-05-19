
def get_birthstone(month):
  mon_birthstone = {}
  source = '/static/'
  if (month == 'jan'):
    source += 'jan_garnet.jpg'
    bstone = "Garnet"
    mon = "January"
    mon_birthstone["month"] = "January"
    mon_birthstone["stone"] = "Garnet"
    mon_birthstone["image"] = source
  elif (month == 'feb'):
    source += 'feb_amethyst.jpg'
    bstone = "Amethyst"
    mon = "February"
  elif (month == 'mar'):
    source += 'mar_aquamarine.jpg'
    bstone = "Aquamarine"
    mon = "March"
  elif (month == 'apr'):
    source += 'apr_diamond.jpg'
    bstone = "Diamond"
    mon = "April"
  elif (month == 'may'):
    source += 'may_emerald.jpg'
    bstone = "Emerald"
    mon = "May"
  else:
    source += 'may_emerald.jpg'
  return mon_birthstone