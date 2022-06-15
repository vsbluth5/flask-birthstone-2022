
def get_birthstone(month):
  birthstone_dict = {}
  source = 'static/images/'
  if (month == 'jan'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "January"
    birthstone_dict["name"] = "Garnet"
    birthstone_dict["source"] = source
  elif (month == 'feb'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "February"
    birthstone_dict["name"] = "Amethyst"
    birthstone_dict["source"] = source
  elif (month == 'mar'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "March"
    birthstone_dict["name"] = "Aquamarine"
    birthstone_dict["source"] = source
  elif (month == 'apr'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "April"
    birthstone_dict["name"] = "Diamond"
    birthstone_dict["source"] = source
  elif (month == 'may'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "May"
    birthstone_dict["name"] = "Emerald"
    birthstone_dict["source"] = source
  elif (month == 'june'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "June"
    birthstone_dict["name"] = "Pearl"
    birthstone_dict["source"] = source
    elif (month == 'july'):
    source += 'jan_garnet.webp'
    birthstone_dict["month"] = "July"
    birthstone_dict["name"] = "Pearl"
    birthstone_dict["source"] = source
  return birthstone_dict