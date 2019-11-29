
require(rvest)

page <- "https://www.transfermarkt.us/premier-league/marktwertaenderungen/wettbewerb/GB1/pos//detailpos/0/verein_id/0/land_id/0"

scraped_page <- read_html(page)

PlayerNames  % html_nodes("#yw2 .spielprofil_tooltip") %>% html_text() #%>% as.character()
TransferValue % html_nodes(".rechts.hauptlink a") %>% html_text() %>% as.character()

df <- data.frame(PlayerNames, TransferValue)

head(df)