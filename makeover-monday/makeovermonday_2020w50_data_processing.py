import pandas as pd

data = pd.read_csv("elements-by-episode.csv", encoding='UTF16', sep="\t")

# Remove data for paintings by guests

guest_eps = data[(data.Element == "Guest") & (data.Included == 1)].Episode
df = data[(~data.Episode.isin(guest_eps))]

# Reformat data for generating word cloud in Tableau

titles = df[df.Element == "Barn"].Title.tolist()
df_titles = pd.DataFrame(" ".join(titles).split(" "))
df_titles.columns = ['word']

# Combine similar words

df_titles = df_titles.replace(['WATERFALL', 'FALLS'],'WATERFALL')
df_titles = df_titles.replace(['DAISY', 'DAISIES'],'DAISY')
df_titles = df_titles.replace(["EVENING'S", 'EVENING'],'EVENING')
df_titles = df_titles.replace(['FROSTY', 'FROST'],'FROST')
df_titles = df_titles.replace(['GRAY', 'GREY'],'GREY')
df_titles = df_titles.replace(['HIDE-A-WAY', 'HIDE-AWAY', 'HIDEAWAY'],'HIDEAWAY')
df_titles = df_titles.replace(['HORIZON', 'HORIZONS'],'HORIZON')
df_titles = df_titles.replace(['MIST', 'MISTY'],'MIST')
df_titles = df_titles.replace(['MORN', 'MORNING'],'MORNING')
df_titles = df_titles.replace(['MOUNTAIN', 'MOUNTAINS', 'MT.', 'PEAKS'],'MOUNTAIN')
df_titles = df_titles.replace(['NATURE', "NATURE'S"],'NATURE')
df_titles = df_titles.replace(['PEACE', 'PEACEFUL'],'PEACE')
df_titles = df_titles.replace(["RIVER'S", 'RIVER'],'RIVER')
df_titles = df_titles.replace(['SEA', 'SEAS'],'SEA')
df_titles = df_titles.replace(['SECLUDED', 'SECLUSION'],'SECLUDED')
df_titles = df_titles.replace(['SNOW', 'SNOWY', 'SNOWFALL', 'SNOWBOUND'],'SNOW')
df_titles = df_titles.replace(['SPRING', 'SPRINGTIME'],'SPRING')
df_titles = df_titles.replace(["STORM'S", 'STORM', 'STORMY'],'STORM')
df_titles = df_titles.replace(["TRAIL'S", 'TRAIL'],'TRAIL')
df_titles = df_titles.replace(['TRANQUILITY', 'TRANQUIL'],'TRANQUIL')
df_titles = df_titles.replace(['TREE', 'TREES'],'TREE')
df_titles = df_titles.replace(['WINTER', "WINTER'S", 'WINTERTIME'],'WINTER')
df_titles = df_titles.replace(['WOODED', 'WOODS'],'WOODS')
df_titles = df_titles.replace(['SEA', 'SEASCAPE', 'SEASIDE', 'OCEAN'],'SEA')
df_titles = df_titles.replace(['RIVERSIDE', 'RIVER'],'RIVER')
df_titles = df_titles.replace(['ROADSIDE', 'ROAD'],'ROAD')
df_titles = df_titles.replace(['FALL', 'AUTUMN'],'AUTUMN')
df_titles = df_titles.replace(['EVERGREEN', 'EVERGREENS'],'EVERGREEN')
df_titles = df_titles.replace(['GOLD', 'GOLDEN'],'GOLD')
df_titles = df_titles.replace(['COLOR', 'COLORS'], 'COLOR')
df_titles = df_titles.replace(['DAWN', "DAWN'S"], 'DAWN')
df_titles = df_titles.replace(['DAY', "DAY'S", 'DAYS'], 'DAY')
df_titles = df_titles.replace(['DELIGHT', "DELIGHTFUL"], 'DELIGHT')
df_titles = df_titles.replace(['LIGHT', "LIGHTS"], 'LIGHT')
df_titles = df_titles.replace(['MAJESTIC', "MAJESTY"], 'MAJESTIC')
df_titles = df_titles.replace(['PATH', "PATHWAY"], 'PATH')

df_titles.to_csv("elements-by-episode_titles.csv")

