import moviesChild
import seriesChild
import fresh_tomatoes

toy_story = moviesChild.Movie("Toy Story",
                              "test",
                              "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "https://youtube.com/watch?v=vwyZH85NQC4", "120")

o_invasor = moviesChild.Movie("O Invasor",
                              "O INVASOR narra a historia de tres amigos companheiros" +
                              " desde os tempos de faculdade de engenharia " +
                              "que sao socios em uma construtora ha mais de 15 anos. Tudo corre bem ate" +
                              " o dia em que um desentendimento na conducao dos negocios os coloca em conflito",
                              "https://upload.wikimedia.org/wikipedia/pt/b/b8/O_Invasor.jpg",
                              "https://www.youtube.com/watch?v=O4wZgt0eiWg", "120")

things_i_hate = moviesChild.Movie("10 Things I Hate About You",
                                  "A pretty, popular teenager can't go out on a date until her " +
                                  "ill-tempered older sister does.",
                                  "https://upload.wikimedia.org/wikipedia/pt/7/76/10_Things_I_Hate_About_You.jpg",
                                  "https://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjNhJTnjcrQAhUBEZAKHWYjD8QQtwIIIDAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAWmjzCZr0Jw&usg=AFQjCNESEvQOoFrbwr8JCtGAFt93mg_UOg&sig2=uqpeFb3bNKv661sl84legg", # NOQA
                                  "120")

sucker_punch = moviesChild.Movie("Sucker Punch",
                                 "A young girl is institutionalized by her abusive stepfather." +
                                 " Retreating to an alternative reality as a coping strategy, " +
                                 "she envisions a plan which will help her escape from the mental facility.",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9f/Sucker_Punch_film_poster.jpg",
                                 "https://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjKsaOCjsrQAhVCx5AKHWpyCrwQuAIIITAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DXAnnWoXD2tI&usg=AFQjCNFd67-yrLugqZ2QJ20GlSw5LucCIg&sig2=9MVngMZhY5PVKAIXUSpAqQ", # NOQA
                                 "120")

carandiru = moviesChild.Movie("Carandiru",
                              "Brazilian MD Drauzio Varella starts AIDS prevention in Brazil's largest prison, " +
                              "Carandiru, in Sao Paulo, where the population is nearly double its 4,000 maximum.",
                              "https://filmesnobrasil.files.wordpress.com/2013/07/carandiru.jpg",
                              "https://www.youtube.com/watch?v=5C0mR2tfWMU",
                              "120")

sunshine_mind = moviesChild.Movie("Eternal Sunshine of the Spotless Mind",
                                  "When their relationship turns sour, a couple undergoes a procedure" +
                                  " to have each other erased from their memories. But it is only through the " +
                                  "process of loss that they discover what they had to begin with.",
                                  "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg", # NOQA
                                  "https://www.youtube.com/watch?v=yE-f1alkq9I", "120")

ricky_and_morty = seriesChild.Series("Rick and Morty",
                                     "teste",
                                     "http://www.gstatic.com/tv/thumb/tvbanners/11928964/p11928964_b_v8_aa.jpg",
                                     "https://www.youtube.com/watch?v=eOBoKxEcVAA", "120")

trailer_park_boys = seriesChild.Series("Trailer Park Boys",
                                       "Trailer Park Boys is a Canadian mockumentary television series " +
                                       "created and directed by Mike Clattenburg that focuses on the" +
                                       " misadventures of a group of trailer park residents, some of" +
                                       " whom are ex-convicts, living in the fictional " +
                                       "Sunnyvale Trailer Park in Dartmouth, Nova Scotia.",
                                       "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR-xKuiQMebZ2MRXT_yGvjptP_2BB9DYtfbguPBKY85NbafDREl1Fs3fg", # NOQA
                                       "https://www.youtube.com/watch?v=IKtT_QtmyQE", "30")

seinfeld = seriesChild.Series("Seinfeld",
                              "Seinfeld is an American sitcom that originally ran for nine seasons" +
                              " on NBC, from 1989 to 1998. It was created by Larry David and " +
                              "Jerry Seinfeld, the latter starring as a fictionalized version of " +
                              "himself. Set predominantly in an apartment building in Manhattan's " +
                              "Upper West Side in New York City (although taped entirely in Los Angeles)," +
                              " the show features a handful of Jerry's friends and acquaintances, particularly " +
                              "best friend George Costanza (Jason Alexander), former girlfriend Elaine Benes " +
                              "(Julia Louis-Dreyfus), and neighbor across the hall Cosmo Kramer (Michael Richards)." +
                              " It is often described as being 'a show about nothing', as many of " +
                              "its episodes are about the minutiae of daily life.",
                              "http://www.sonypictures.com/tv/seinfeld/assets/images/onesheet.jpg",
                              "https://www.youtube.com/watch?v=PaPxSsK6ZQA", "20")

movies = [toy_story, o_invasor,
          things_i_hate, sucker_punch,
          carandiru, sunshine_mind]

series = [ricky_and_morty, trailer_park_boys,
          seinfeld]

fresh_tomatoes.open_movies_page(movies, series)