# mobex_watcher

Um script para acompanhar as modificações que acontecem em uma parte específica do site da Universidade Federal do estado do Pará. Uma vez por semana ele verifica as paginas, faz um scraping com [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) nas partes de interesse, monta um email e envia pelo [Sendgrid](https://sendgrid.com) graças ao [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler).
