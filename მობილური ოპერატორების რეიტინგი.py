#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="images/ASA_Mobile_123.png" width="300" alt="ASA Mobile Companies Ranking 123 logo" />
# </center>

# # მობილური ოპერატორების რეიტინგი საქართველოში

# In[1]:


from IPython.display import display, HTML

display(HTML("""<img alt="მობილური ოპერატორების ყოველწლიური რეიტინგი საქართველოში" src="ranking.png"></img>"""))


# # მობილური ოპერატორების ყოველწლიური რეიტინგები
# 
# მობილური ოპერატორების მოცემული ყოველწლიური რეიტინგები შედგენილია სპეციალური საზომის, "მიმზიდველობის კოეფიციენტი-ს" გამოყენებით, რომელიც ეყრდნობა მობილური აბონენტების მიერ ფაქტობრივად განხორციელებულ არჩევანს ბაზარზე არსებულ კომპანიებს შორის, ანუ სტატისტიკურ მონაცემებს იმის შესახებ თუ რომელი ოპერატორის სიმ ბარათს ირჩევენ მობილური აბონენტები. შესაბამისად, ეს რეიტინგი წლების მიხედვით გვიჩვენებს, ამა თუ იმ წელს რომელი მობილური ოპერატორი იყო უფრო მიმზიდველი და მაღალრეიტინგული მომხმარებლების თვალში. ზემოთ წარმოდგენილია ამ რეიტინგების ვიზუალიზაცია წლების მიხედვით, შესაბამისი წლის საუკეთესო სამეული (პირველი, მეორე და მესამე ადგილები) თითოეული წლისთვის გამოსახულია გრაფიკულად. ამ რეიტინგის შედგენის პროცესის ყველა დეტალი, მოცემული ყოველწლიური რეიტინგის შესადგენად გამოყენებული "მიმზიდველობის კოეფიციენტი-ს" მათემატიკური ფორმულა და შესაბამისი Python-კოდი სრულიად ღია სახით შეგიძლიათ იხილოთ ამავე დოკუმენტის [ინგლისურენოვან ვერსიაში](../).
# 
# 
# 
# განსაზღვრებები:
#  - **მობილური აბონენტი** (როგორც განსაზღვრულია კომუნიკაციების კომისიის მიერ) – მობილური კომუნიკაციების აბონენტად განიხილება SIM ბარათი, რომლის გამოყენებითაც თვის (კვარტლის,წლის) განმავლობაში ერთხელ მაინც განხორციელდა ან მიღებულ იქნა ხმოვანი ზარი, SMS, MMS, გაწეულ იქნა ინტერნეტით ან სხვა დამატებითი სერვისით მომსახურება, ან დაირიცხა სააბონენტო გადასახადი (კომპანიის თანამშრომლების ჩათვლით და სატესტო ბარათების ჩაუთვლელად).
# 
# 
# 
# გამოყენებული მონაცემები:
# - მობილური აბონენტების სტატისტიკური მონაცემები კომპანიების მიხედვით მოპოვებულია 2022 წლის 18 მაისს საქართველოს კომუნიკაციების კომისიის ვებსაიტიდან: [comcom.ge](https://comcom.ge).
# 

# In[2]:


get_ipython().run_cell_magic('HTML', '', "<style>\n@media (max-width: 540px) {\n  .output .output_subarea {\n    max-width: 100%;\n  }\n}\n</style>\n<script>\n  $( document ).ready(function(){\n    $('div.input').hide();\n  });\n</script>\n")


# In[3]:


get_ipython().run_cell_magic('capture', '', '%mkdir OGP_classic_ka\n')


# In[4]:


get_ipython().run_cell_magic('capture', '', '%%file "OGP_classic_ka/conf.json"\n{\n  "base_template": "classic",\n  "preprocessors": {\n    "500-metadata": {\n      "type": "nbconvert.preprocessors.ClearMetadataPreprocessor",\n      "enabled": true,\n      "clear_notebook_metadata": true,\n      "clear_cell_metadata": true\n    },\n    "900-files": {\n      "type": "nbconvert.preprocessors.ExtractOutputPreprocessor",\n      "enabled": true\n    }\n  }\n}\n')


# In[5]:


get_ipython().run_cell_magic('capture', '', '%%file "OGP_classic_ka/index.html.j2"\n{%- extends \'classic/index.html.j2\' -%}\n{%- block html_head -%}\n\n{#  OGP attributes for shareability #}\n<meta property="og:url"          content="https://sentinel-1.github.io/mobile_subscribers_Georgia/ka/" />\n<meta property="og:type"         content="article" />\n<meta property="og:title"        content="მობილური ოპერატორების რეიტინგი საქართველოში" />\n<meta property="og:description"  content="რომელ კომპანიებს ირჩევენ მობილური კომუნიკაციების აბონენტები?" />\n<meta property="og:image"        content="https://raw.githubusercontent.com/sentinel-1/mobile_subscribers_Georgia/master/images/ASA_Mobile_123.png" />\n<meta property="og:image:alt"    content="მობილური ოპერატორების რეიტინგის 123 ლოგო" />\n<meta property="og:image:type"   content="image/png" />\n<meta property="og:image:width"  content="1200" />\n<meta property="og:image:height" content="628" />\n    \n<meta property="article:published_time" content="2022-08-14T05:23:44+00:00" />\n<meta property="article:modified_time"  content="{{ resources.iso8610_datetime_utcnow }}" />\n<meta property="article:publisher"      content="https://sentinel-1.github.io" />\n<meta property="article:author"         content="https://github.com/sentinel-1" />\n<meta property="article:section"        content="datascience" />\n<meta property="article:tag"            content="datascience" />\n<meta property="article:tag"            content="Python" />\n<meta property="article:tag"            content="data" />\n<meta property="article:tag"            content="analytics" />\n<meta property="article:tag"            content="datavisualization" />\n<meta property="article:tag"            content="bigdataunit" />\n<meta property="article:tag"            content="visualization" />\n<meta property="article:tag"            content="mobilesubscribers" />\n<meta property="article:tag"            content="mobilecompanies" />\n<meta property="article:tag"            content="ranking" />\n<meta property="article:tag"            content="telecomunication" />\n\n\n<link rel="icon" type="image/x-icon" href="../../favicon.ico">\n\n{{ super() }}\n\n{%- endblock html_head -%}\n    \n    \n{% block body_header %}\n<body>\n    \n<div class="container">\n  <nav class="navbar navbar-default">\n    <div class="container-fluid">\n      <ul class="nav nav-pills  navbar-left">\n        <li role="presentation">\n          <a href="/ka/">\n            <svg xmlns="http://www.w3.org/2000/svg"\n                 viewBox="0 0 576 512" width="1em">\n              <path \n                fill="#999999"\nd="M 288,0 574,288 511,288 511,511 352,511 352,352 223,352 223,511 62,511 64,288 0,288 Z"\n              />\n            </svg> მთავარი\n          </a>\n        </li>\n      </ul>\n      <ul class="nav nav-pills  navbar-right">\n        <li role="presentation">\n          <a href="/mobile_subscribers_Georgia/">🇬🇧 English </a>\n        </li>\n        <li role="presentation" class="active">\n          <a href="/mobile_subscribers_Georgia/ka/">🇬🇪 ქართული</a>\n        </li>\n      </ul>\n    </div>\n  </nav>\n</div>\n\n\n\n  <div tabindex="-1" id="notebook" class="border-box-sizing">\n    <div class="container" id="notebook-container">    \n{% endblock body_header %}\n\n{% block body_footer %}\n    </div>\n  </div>\n  <footer>\n    <div class="container"\n         style="display:flex; flex-direction: row; justify-content: center; align-items: center;">\n      <p style="margin: 3.7em auto;"> © 2022\n        <a href="https://github.com/sentinel-1" target="_blank">Sentinel-1</a>\n      </p>\n      <!-- TOP.GE ASYNC COUNTER CODE -->\n      <div id="top-ge-counter-container" data-site-id="116052"\n           style="margin-right: 3.7em;float: right;"></div>\n      <script async src="//counter.top.ge/counter.js"></script>\n      <!-- / END OF TOP.GE COUNTER CODE -->\n      <!-- ANALYTICS.LAGOGAL.COM -->\n      <div id="analytics-lagogal-com-access" data-site-id="20221"\n           style="margin: 0;padding: 0;"></div>\n      <script async src="//analytics.lagogal.com/access.js"></script>\n      <!-- / END OF ANALYTICS.LAGOGAL.COM -->\n     </div>\n  </footer>\n</body>\n{% endblock body_footer %}\n')


# 
# *მოცემული დოკუმენტი თავდაპირველად გამოქვეყნებულ იქნა Apache License (Version 2.0) ლიცენზიით შემდეგ GitHub რეპოზიტორზე: [sentinel-1/mobile_subscribers_Georgia](https://github.com/sentinel-1/mobile_subscribers_Georgia)*
# 
# მოცემულ დოკუმენტის ორიგინალ ვერსიასთან დაკავშირებულ საკითხებზე შესაბამისი უკუკავშირისათვის, რჩევებისათვის ან შენიშვნებისთვის (თუ რამეა) შეგიძლიათ ახალი Issue-ს შექმნის გზით დააყენოთ საკითხი მისივე GitHub რეპოზიტორის შესაბამის გვერდზე: [Issues page of the repository](https://github.com/sentinel-1/mobile_subscribers_Georgia/issues)
