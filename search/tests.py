from django.test import TestCase

# Create your tests here.
import requests
import json
kw = 'sofa'
num = 0
engine = 'google'
# url = "http://47.252.3.225:8080/getweb/?kw=%s&num=%s&engine=%s" % (kw,num,engine)
url = "http://47.252.3.225:8080/get_web/?kw=%s&num=%s&engine=%s" % (kw,num,engine)
url = "http://127.0.0.1:8000/get_web/?kw=%s&num=%s&engine=%s" % (kw,num,engine)

ret = requests.get(url,)
result = ret.content.decode()
print(result)
# result = '''{"data": [{"title": "Sofas, Sofa Beds, Couches IKEA - Sofa designed for comfort", "website": "https://www.ikea.com.hk/en/products/sofas-and-armchairs/sofas", "description": "Buy sofas, sofa beds, armchairs to create the perfect solution for your living room. We have sofas available in different materials, colours and styles to fit any\u00a0...", "mail": null}, {"title": "Buy Designer Sofas Online in Hong Kong at ... - SofaSale", "website": "https://www.sofasale.com.hk/furniture/sofas", "description": "Buy European quality sofa at Sofa Sale. Browse our selection of designer Sofas, fabric sofas, leather sofa, L shape sofas, sofa bed, patchwork sofas, baroque\u00a0...", "mail": null}, {"title": "Modern designer Sofas - BoConcept", "website": "https://www.boconcept.com/en-gb/shop/sofas", "description": "Love the freedom of a modular sofa? Or do you require your sofa to have room for lounging or even to function as a sofa bed? Our contemporary sofas can be\u00a0...", "mail": "louise@boconceptwestchester.com;last@boconcept.com;franchise@boconcept.com"}, {"title": "Sofa \u2013 Francfranc Hong Kong", "website": "https://hk.francfranc.net/collections/sofa", "description": "Products 1 - 60 of 69 \u2014 PIONI SOFA LIGHT BLUE X WHITE. HK$4,500.00 ... FLEURETTE SOFA DARK GRAY. HK$5,800.00 ... PIONI SOFA NAVY X NATURAL.", "mail": null}, {"title": "Sofas - Minotti", "website": "https://www.minotti.com/en/sofas", "description": "View all; \u6c99\u53d1; \u8eba\u6905; \u9760\u6905; \u914d\u4ef6; \u5ea7\u6905\u4e0e\u6905\u51f3; \u684c\u5b50; \u8336\u51e0; \u684c\u53f0; \u4e66\u67dc\u4e0e\u7f6e\u7269\u67dc; \u5730\u6bef; \u5e8a\u5177; \u5367\u5ba4\u7f6e\u7269\u67dc; \u914d\u5957\u7ec7\u7269. Connery \u00b7 Torii \u00b7 Blazer \u00b7 Mattia \u00b7 Daniels \u00b7 West.", "mail": "librarian@ddcnyc.com;mail@spenceandlyda.com;minotti@lapp.in2p3"}, {"title": "Designer Sofas online | MADE.com", "website": "https://www.made.com/sofas-and-armchairs/sofas", "description": "Looking for a high quality sofa but don't want to break the bank? Discover our fantastic range of design sofas super comfy and affordable. Pay in 3 available.", "mail": "first_initial@made.com;service-client@made.com;julien@made.com"}, {"title": "Furniture and Decor Online Buy Quality Sofa ... - Indigo Living", "website": "https://www.indigo-living.com/hk_en/furniture/living-room/sofas.html", "description": "Your sofa should be comfortable, stylish and ready to spend many years in your home. That's why Indigo Living offers a wide selection of chic sofas to fit any room.", "mail": null}, {"title": "Sofas - HOMELESS.hk", "website": "https://homeless.hk/collections/sofa", "description": "Muuto Outline Sofa 3-Seater Black Base , Refine Leather Cognac $58,995.00 ... Muuto Outline sofa chaise longue, black base, right from $51,495.00.", "mail": null}, {"title": "Sofas - Muuto", "website": "https://www.muuto.com/products/sofas/", "description": "From simple lines over elegant shapes to sculptural forms, our sofa collection brings our ideas of modern, Scandinavian design into any space through modern\u00a0...", "mail": "CUSTOMERCARE@MUUTO.COM;first@muuto.com"}]}'''
if result == 'no data' or result == 'engine error':
    data = {}
else:
    s = json.loads(result)
    print(s)
    print(type(s))

    with open('ret.json','w',encoding='utf-8') as f:
        json.dump(s,f,indent=4,ensure_ascii=False)
    # print(ret.content)
    # print(ret)
    # print(ret.content.decode())