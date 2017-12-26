# icowatchlist-api
A semi useful hack together of icowatchlist's data for a tool I'm working on for security related things for ico's.
I wrote this fast never planned a public release but why not incase it's actually needed as I couldnt find one.

Also note it wasnt optimized at all may not be very pythonic, so if You see an issue please request a update.


and an example of running it would be like this

python api.py -l live

python api.py -f finished

python api.py -f upcoming


It will return 2 lists for you with the names of the icos and there Links
While im aware the links are returned in a weird format they are storing the real link inside of the response headers
so cloudflare cdn is blocking even on 30 seconds timer per url

so I am in talks with the creator of a flare bypass library for permission to use and mostly icowatchlist's permission to scrape the api that way as it could violate there tos.
