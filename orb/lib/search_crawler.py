

def is_search_crawler(user_agent):
    spiders = {'Googlebot',
               'Yammybot',
               'Openbot',
               'Yahoo',
               'Slurp',
               'msnbot',
               'ia_archiver',
               'Lycos',
               'Scooter',
               'AltaVista',
               'Teoma',
               'Gigabot',
               'Googlebot-Mobile',
               'MJ12bot',
               'bingbot',
               'LinkedInBot',
               'baiduspider',
               'facebookexternalhit',
               'spider',
               'domainreanimator.com',
               'seznambot',
               'ahrefsbot',
               'spbot',
               'wbsearchbot',
               'dotbot',
               'betabot',
               'Python-urllib',
               'Twitterbot',
               'YandexBot',
               'Exabot',
               }
    for s in spiders:
        if s.lower() in user_agent.lower():
            return True
    return False
