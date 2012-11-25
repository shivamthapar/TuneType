def getVideo(artist, song):
	try:
		import gdata.youtube
		import gdata.youtube.service

		yt_service = gdata.youtube.service.YouTubeService()
		search_terms= song+" "+artist+" lyrics"

		# Turn on HTTPS/SSL access.
		# Note: SSL is not available at this time for uploads.
		yt_service.ssl = True
		yt_service.developer_key = 'AI39si7JIjRfBh_5-WURCpWRmNJU5BgGzKVfUjICv1ZYaxzt5b0gs14loDF3S4wwrsWcy0PBsFjgo17SmTDa65lVEjcmwo6iMg'
		query = gdata.youtube.service.YouTubeVideoQuery()
		query.vq = search_terms
		query.orderby = 'relevance'
		query.racy = 'include'
		feed = yt_service.YouTubeQuery(query)
		return feed.entry[0]
	except:
		pass