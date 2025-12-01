import pandas as pd
import matplotlib.pyplot as plt

#load the data
df= pd.read_csv('netflix_titles.csv')

#clean the data
df= df.dropna(subset=['type','duration','country','release_year','rating','listed_in','director','title'])

#movies vs tv shows (pie chart)
s_type= df['type'].value_counts()
plt.bar(s_type.index, s_type.values, color= ['#1f77b4','#17becf'])
plt.title('Movies vs TV Shows in Netflix')
plt.xlabel('Type')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Movies vs TV Shows in Netflix.png', dpi=300,bbox_inches='tight')
plt.show()


#content rating (bar graph)
content_rating= df['rating'].value_counts()
plt.barh(content_rating.index, content_rating.values, color='#2ca02c')
plt.title('Distribution of Content Ratings on Netflix')
plt.ylabel('Content in Netflix')
plt.xlabel('Content Rating')
plt.tight_layout()
plt.savefig('Distribution of Content Ratings on Netflix.png', dpi=300,bbox_inches='tight')
plt.show()


#movie duration
movie_dr= df[df['type']=='Movie'].copy()
movie_dr['int']= movie_dr['duration'].str.replace('min','').astype('int')
plt.hist(movie_dr['int'], bins=35, color='#9467bd', edgecolor='black')
plt.title('Distribution of Movie Duration on Netflix')
plt.xlabel('Movies (in minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('Distribution of Movie Duration on Netflix.png', dpi=300,bbox_inches='tight')
plt.show()


#release year vs number of contents
release_year=  df['release_year'].value_counts().sort_index()
plt.plot(release_year.index, release_year.values,color='#17becf')
plt.title('Content Released per Year on Netflix')
plt.xlabel('Year of Release')
plt.ylabel('Number of Content')
plt.tight_layout()
plt.savefig('Content Released per Year on Netflix.png', dpi=300,bbox_inches='tight')
plt.show()


#top 10 countries
df['cnt']=df['country'].str.split(',').apply(lambda x: [i.strip() for i in x])
cont= df['cnt'].explode()
top_cnt= cont.value_counts().head(10)
plt.barh(top_cnt.index, top_cnt.values, color='#1f77b4')
plt.title('Top 10 Countries with the Most Netflix Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Countries Name')
plt.tight_layout()
plt.savefig('Top 10 Countries with the Most Netflix Titles.png', dpi=300,bbox_inches='tight')
plt.show()


#most viewed genre
df['genre']= df['listed_in'].str.split(',').apply(lambda x: [i.strip() for i in x])
zonra= df['genre'].explode()
zon= zonra.value_counts().head(10)
plt.barh(zon.index, zon.values, color= '#17becf')
plt.title('Top 10 Genres on Netflix')
plt.ylabel('Genre')
plt.xlabel('Number of Shows')
plt.tight_layout()
plt.savefig('Top 10 Genres on Netflix.png', dpi=300,bbox_inches='tight')
plt.show()


#which top 5 director has maximum title
df['dir']=df['director'].str.split(',')
dire= df['dir'].explode()
direc= dire.value_counts().head(5)
plt.barh(direc.index, direc.values, color= '#2ca02c')
plt.title('Top 5 Directors with the Most Netflix Titles')
plt.ylabel('Name of Directors')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig('Top 5 Directors with the Most Netflix Titles.png', dpi=300,bbox_inches='tight')
plt.show()