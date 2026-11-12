"""Générateur de la maquette La Maison des Lys (Pizza des Lys). Usage : python build.py <dossier-du-projet>
Contenus relevés sur pizzadeslys.fr (novembre 2026). Rien d'inventé : textes, photos, adresses, horaires, liens de commande."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 5  # cache : incrémenter à chaque changement de CSS ou JS
CARTE = 'https://www.pizzadeslys.fr/_files/ugd/52adf8_3a8d3a2748b94ef480366f6aabeb9721.pdf'
CMD_P = 'https://pizzadeslys.foxorders.fr/'
CMD_H = 'https://hoteldeslys.foxorders.fr/shops'
IG_P = 'https://www.instagram.com/pizza_deslys/'
IG_H = 'https://www.instagram.com/hotel_des_lys/'

# les trois adresses (site pizzadeslys.fr)
R = {
    'peronnas': dict(nom='Pizza des Lys', ville='Péronnas', adr='833 avenue de Lyon, 01960 Péronnas', tel='04 74 32 61 61',
                     hor=[('Lundi au samedi', '11 h 30 – 14 h · 18 h – 22 h'), ('Dimanche', '18 h 30 – 21 h 30')], cmd=CMD_P, img='p13', ig=IG_P),
    'bourg': dict(nom='Au Petit des Lys', ville='Bourg-en-Bresse', adr='18 cours de Verdun, 01000 Bourg-en-Bresse', tel='04 74 50 07 38',
                  hor=[('Mardi au samedi', '11 h – 14 h · 18 h – 22 h')], cmd=None, img='p26', ig=IG_P),
    'chatillon': dict(nom='Hôtel des Lys', ville='Châtillon-sur-Chalaronne', adr='Place du Champ de Foire, 01400 Châtillon-sur-Chalaronne', tel='04 74 23 95 97',
                      hor=[('Mardi au samedi', '9 h – 23 h')], cmd=CMD_H, img='p46', ig=IG_H),
}
PAGE = {'peronnas': 'peronnas.html', 'bourg': 'bourg.html', 'chatillon': 'chatillon.html'}
NAV = [('peronnas.html', 'Péronnas'), ('bourg.html', 'Bourg'), ('chatillon.html', 'Châtillon'), ('histoire.html', 'Notre histoire')]


def th(t):
    return 'tel:' + t.replace(' ', '')


def pill(t, href, cls='', arrow='↗', ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="pill {cls}" href="{href}"{x}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}logo.svg" alt=""><span><span class="wm">La Maison <i>des Lys</i></span><small>Pizzas · 3 adresses</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('reserver.html', 'Réserver', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#140c08">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="La Maison des Lys, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{CMD_P}" target="_blank" rel="noopener" aria-label="Commander en ligne"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 2 21h20L12 2zm0 5.2 6.4 11.8H5.6L12 7.2z" fill="currentColor"/><circle cx="10" cy="15" r="1.3" fill="currentColor"/><circle cx="13.6" cy="12.6" r="1.1" fill="currentColor"/><circle cx="14" cy="16.6" r="1" fill="currentColor"/></svg><span>Commander</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    adr = ''.join(f'<li><a href="{PAGE[k]}">{r["nom"]}</a> · {r["ville"]}</li>' for k, r in R.items())
    tels = ''.join(f'<li><a href="{th(r["tel"])}">{r["tel"]}</a> · {r["ville"]}</li>' for r in R.values())
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Trois adresses, une seule mission : partager l’amour du bon, de l’authentique et du généreux. Depuis le premier camion à pizza de Bourg-en-Bresse.</p></div>
<div><h4 class="micro">Nos restaurants</h4><ul>{adr}<li><a href="histoire.html#distributeurs">Distributeurs 24 h/24</a></li></ul></div>
<div><h4 class="micro">Appeler</h4><ul>{tels}</ul></div>
<div><h4 class="micro">Suivre</h4><ul><li><a href="{IG_P}" target="_blank" rel="noopener">Instagram Pizza des Lys</a></li><li><a href="{IG_H}" target="_blank" rel="noopener">Instagram Hôtel des Lys</a></li><li><a href="{CARTE}" target="_blank" rel="noopener">La carte (PDF)</a></li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">DES LYS</div>
<div class="fb micro"><span class="pad">© La Maison des Lys</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Une envie <em>de pizza ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Sur place · à emporter · 24 h/24</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Réserver une table', 'reserver.html', 'blue')}{pill('Commander en ligne', CMD_P, 'ghost', ext=True)}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def hor(r):
    return '<div class="hor rv">' + ''.join(f'<span><b>{j}</b> : {h}</span>' for j, h in r['hor']) + '<span class="micro">Horaires à confirmer avec le restaurant</span></div>'


def resto(key, title, desc, h1, lead, img2, intro_h, intro_p, checks, photos, more=''):
    r = R[key]
    btn = pill('Commander en ligne', r['cmd'], 'blue', ext=True) if r['cmd'] else pill(f'Commander : {r["tel"]}', th(r['tel']), 'blue')
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{btn}{pill("Réserver une table", "reserver.html?r=" + key, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, PAGE[key]) + pagehead(r['ville'], h1, lead, f'{PH}{r["img"]}.webp', f'{PH}{img2}.webp', extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">{r['nom']}</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">En images</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">À table <em>chez nous</em></h2>{gal(photos)}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Où nous trouver ?</span><h2 class="sp">{r['ville']}</h2>
<p class="lead rv" style="margin-top:1.4rem">{r['adr']}</p>{hor(r)}</div>
<div class="rv"><div class="contactline" style="margin-bottom:1.6rem"><a href="{th(r['tel'])}">{r['tel']}</a></div><div class="row" style="display:flex;gap:10px;flex-wrap:wrap">{pill('Voir la carte', CARTE, 'blue', ext=True)}{pill('Instagram', r['ig'], 'ghost', ext=True)}</div></div></div></section>''' + cta() + foot()


def pages():
    P = {}
    hero_tiles = [('t1', 'p04'), ('t2', 'p18'), ('t3', 'p28'), ('t4', 'p42'), ('t5', 'p24'), ('t6', 'p38'), ('t7', 'p13')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['p48', 'p49', 'p24', 'p19', 'p31', 'p51', 'p36', 'p38'])
    wall_imgs = ['p19', 'p28', 'p20', 'p29', 'p21', 'p37', 'p23', 'p45', 'p32', 'p41', 'p31', 'p36']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [(PAGE[k], f'0{i + 1}', r['nom'], f'{r["ville"]}. ' + d, r['img'], b) for i, ((k, r), d, b) in enumerate(zip(R.items(), [
        'Le restaurant où tout a commencé. Distributeur 24 h/24 juste à côté.',
        'En plein centre-ville, une grande salle lumineuse à l’étage.',
        'Restaurant, bar à cocktails, terrasse ensoleillée et 7 chambres.'], ['Sur place · emporter', 'Midi · soir', 'Restaurant · hôtel']))]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>{b}</b></span></a>' for h, n, t, d, _, b in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [
        ('p28', 'Pizzas maison'), ('p29', 'Pâtes à la truffe'), ('p21', 'Burger'), ('p37', 'Plats généreux'), ('p30', 'Côté bar'), ('p32', 'Salades')])
    steps = [('Sur place', 'Le midi et le soir, dans l’une de nos trois salles.'),
             ('À emporter', 'Commandez en ligne ou par téléphone, passez la chercher.'),
             ('24 h/24', 'Nos distributeurs autour de Bourg-en-Bresse, jour et nuit.'),
             ('Fidélité', 'La 10e pizza est offerte avec votre carte de fidélité.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Pizzas maison', 'Pâtes à la truffe', 'Belles viandes', 'Cocktails', 'Terrasse', '24 h/24'] * 2)
    deco = ''.join(f'<img class="ing {c}" src="{PH}{n}.webp" alt="" aria-hidden="true">' for n, c in [('basilic', 'i1'), ('tomates', 'i2'), ('piment', 'i3'), ('oignon', 'i4')])

    P['index.html'] = head('La Maison des Lys — Pizzas maison à Péronnas, Bourg-en-Bresse et Châtillon-sur-Chalaronne', 'Pizza des Lys, Au Petit des Lys, Hôtel des Lys : trois adresses dans l’Ain pour des pizzas maison, des pâtes à la truffe et de belles viandes. Sur place, à emporter, distributeurs 24 h/24.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Pizzas maison</b>plus de 25 recettes</div>
<div class="cap micro c2"><b>3 adresses</b>dans l’Ain</div>
<div class="cap micro c3"><b>24 h/24</b>nos distributeurs</div>
<div class="go">{pill('Réserver une table', 'reserver.html')}</div>
{ht}
<p class="para">Avant d’être une maison… c’était un camion.</p>
<h1 class="word">DES LYS</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">La qualité avant tout</span><h2 class="sp">On ne plaisante pas <em>avec la pizza</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Testé, goûté, ajusté… encore et encore, jusqu’à la meilleure formule : une pâte moelleuse et croustillante, une sauce savoureuse, des ingrédients soigneusement choisis.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Plus de 25 pizzas</b> à la carte.</span></li><li><span><b>De nouvelles recettes</b> tout au long de l’année.</span></li><li><span><b>Sur place ou à emporter</b>, le midi et le soir.</span></li></ul>{pill('Voir la carte', CARTE, 'blue', ext=True)}</div>
<div class="ingw">{tile(PH + 'p04.webp', '', par=8, alt='Pizza jambon, burrata et tomates cerises')}{deco}</div></div></section>

<section class="story"><span class="micro mute m3">Notre histoire</span>
<h2><span class="w">Avant</span> <span class="w">d’être</span> <span class="w">une</span> <span class="w">maison,</span> <span class="w">c’était</span> <span class="w">un</span> <span class="w"><em>camion</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Le premier camion à pizza de Bourg-en-Bresse. Puis trois adresses.</p><span class="micro mute m2">Une histoire de famille</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Une carte qui met tout le monde d’accord</span><h2>Pizzas, pâtes <em>et plus</em></h2>{pill('Voir la carte', CARTE, 'blue', ext=True)}</div></section>

<section class="sec" id="restaurants"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos restaurants</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Trois adresses, <em>une passion</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">À la carte</span><h2>Classiques <em>et créations</em></h2></div>{pill('Voir la carte', CARTE, '', ext=True)}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">En chiffres</span><h2 class="sp">Généreux, <em>par nature</em></h2>
<div class="cnt rv"><div><b data-to="3">0</b><span>adresses : Péronnas, Bourg-en-Bresse, Châtillon-sur-Chalaronne</span></div><div><b data-to="25">0</b><span>pizzas maison à la carte, et plus encore</span></div><div><b data-to="24">0</b><span>heures sur 24 : nos distributeurs ne ferment jamais</span></div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Offre de fidélité</span><h2 class="sp">La 10<sup>e</sup> pizza <em>est offerte</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Demandez votre carte de fidélité dans nos restaurants. Ou : 3 pizzas achetées, une bouteille de limonade offerte. Offres non cumulables.</p>{pill('Commander en ligne', CMD_P, 'blue', ext=True)}</div>{tile(PH + 'p31.webp', '', par=8, alt='Pizza roquette et jambon cru')}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Comme vous voulez</span><h2 class="sp">Quatre façons <em>de se régaler</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    P['peronnas.html'] = resto('peronnas', 'Pizza des Lys — Pizzeria à Péronnas, près de Bourg-en-Bresse', 'Pizza des Lys, 833 avenue de Lyon à Péronnas : plus de 25 pizzas maison, sur place ou à emporter, commande en ligne et distributeur 24 h/24. 04 74 32 61 61.',
        'Là où tout <em>a commencé</em>', 'Au cœur de Péronnas, notre pizzeria vous accueille le midi et le soir, pour un moment gourmand en toute simplicité.', 'p09',
        'La recette <em>Pizza des Lys</em>', 'La passion, la curiosité et le goût du partage. Le tout servi avec le sourire d’une équipe adorable, toujours ravie de vous accueillir.',
        [('Plus de 25 pizzas', 'à la carte, et des plats variés.'), ('Sur place ou à emporter.', 'Commande en ligne ou par téléphone.'), ('Distributeur 24 h/24', 'juste à côté du restaurant.'), ('Nouvelles recettes', 'tout au long de l’année.')],
        [('p18', 'Salle', 'L’enseigne lumineuse, dans la salle'), ('p19', 'Pizzas', 'Pizza maison'), ('p20', 'Plats', 'Des plats variés'), ('p21', 'Plats', 'Burger et frites'), ('p24', 'Pizzas', 'Pizza au basilic frais'), ('p22', 'Salle', 'La salle'), ('p23', 'Plats', 'Assiette gourmande'), ('p13', 'Salle', 'Le restaurant de Péronnas'), ('p09', 'Salle', 'Le comptoir et le mur végétal')])

    P['bourg.html'] = resto('bourg', 'Au Petit des Lys — Restaurant pizzeria à Bourg-en-Bresse, cours de Verdun', 'Au Petit des Lys, 18 cours de Verdun à Bourg-en-Bresse : pizzas maison, pâtes à la truffe, belles pièces de viande. Grande salle à l’étage. 04 74 50 07 38.',
        'En plein <em>centre-ville</em>', 'À deux pas du parking du Champ de Foire, l’adresse parfaite pour un déjeuner entre amis ou un repas d’affaires.', 'p27',
        'Ne vous fiez pas <em>au rez-de-chaussée</em>', 'C’est à l’étage que vous découvrirez notre grande salle lumineuse, idéale pour vos repas en toute convivialité.',
        [('Pâtes à la truffe', 'ultra gourmandes.'), ('Pizzas maison', 'croustillantes.'), ('Belles pièces de viande', 'parfaitement préparées.'), ('Sur place ou à emporter.', 'Commande par téléphone.')],
        [('p26', 'Salle', 'La grande salle à l’étage'), ('p28', 'Pizzas', 'Pizza maison'), ('p29', 'Plats', 'Pâtes à la truffe'), ('p30', 'Bar', 'Côté bar'), ('p31', 'Pizzas', 'Pizza roquette'), ('p32', 'Plats', 'Salade gourmande'), ('p27', 'Salle', 'Une table dressée')])

    hotel = f'''
<section class="sec" id="hotel" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre hôtel</span><h2 class="sp">Dormir au cœur <em>de Châtillon</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">7 chambres confortables, chacune avec sa salle de bain privative et un espace cosy. Pour une halte gourmande, un week-end en amoureux ou un déplacement d’affaires, à deux pas des ruelles animées.</p>
<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap">{pill('Réserver une chambre', 'reserver.html?r=chambre', 'blue')}</div></div>{tile(PH + 'p35.webp', '', par=8, alt='Une chambre de l’Hôtel des Lys')}</div></section>'''
    P['chatillon.html'] = resto('chatillon', 'Hôtel des Lys — Restaurant, bar et hôtel à Châtillon-sur-Chalaronne', 'Hôtel des Lys, place du Champ de Foire à Châtillon-sur-Chalaronne : pizzas maison, pâtes à la truffe, cocktails, grande terrasse et 7 chambres. 04 74 23 95 97.',
        'Une pause gourmande, <em>à toute heure</em>', 'En plein cœur de Châtillon-sur-Chalaronne : restaurant, bar, terrasse ensoleillée et 7 chambres.', 'p42',
        'Une carte <em>et un bar</em>', 'Pâtes à la truffe, belles pièces de viande, plus de 25 pizzas maison. Côté bar, de superbes cocktails pour l’apéritif ou le repas.',
        [('Terrasse ensoleillée', 'et de nombreuses salles.'), ('Grands groupes', 'bienvenus : famille, amis, entreprises.'), ('Sur place ou à emporter.', 'Commande en ligne.'), ('7 chambres', 'en plein centre historique.')],
        [('p46', 'Lieu', 'La façade, place du Champ de Foire'), ('p39', 'Lieu', 'La terrasse'), ('p38', 'Pizzas', 'Pizza burrata'), ('p33', 'Lieu', 'La salle'), ('p37', 'Plats', 'Assiette généreuse'), ('p34', 'Lieu', 'La salle voûtée'), ('p41', 'Pizzas', 'Pizza en terrasse'), ('p45', 'Plats', 'Salade'), ('p40', 'Lieu', 'Un coin cosy'), ('p43', 'Lieu', 'Une table près de la fenêtre'), ('p44', 'Lieu', 'Lumière douce'), ('p36', 'Pizzas', 'Pizzas à partager')], hotel)

    P['histoire.html'] = head('Notre histoire — La Maison des Lys', 'Du premier camion à pizza de Bourg-en-Bresse aux trois adresses de La Maison des Lys : l’histoire de Pierre, de son grand-père, et des distributeurs 24 h/24.', 'histoire.html') + pagehead('Notre histoire', 'Une histoire <em>de famille</em>', 'Avant d’être une maison… c’était un camion. Et pas n’importe lequel.', PH + 'p49.webp', PH + 'p48.webp') + f'''
<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Le grand-père</span><h2 class="sp">Pierre, <em>le pionnier</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Il ose un pari fou pour l’époque : lancer le premier camion à pizza de Bourg-en-Bresse, Pizza Home. Chaque soir, son four à bois fait danser les flammes et régale tout un quartier.</p></div>{tile(PH + 'p48.webp', '', par=8, alt='Photo d’archive de la famille')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Le petit-fils</span><h2 class="sp">Pierre, <em>la relève</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Il a gardé en lui la pâte qui lève, la sauce qui mijote, les clients qui repartent le sourire aux lèvres. Avec son associé, il ouvre trois adresses, réunies sous le nom La Maison des Lys.</p></div>{tile(PH + 'p50.webp', '', par=8, alt='Devant l’Hôtel des Lys')}</div></section>
<section class="sec" id="distributeurs" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos distributeurs</span><h2 class="sp">Des pizzas <em>24 h/24</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Préparées dans notre pizzeria, avec le même soin, puis placées dans nos distributeurs autour de Bourg-en-Bresse. Une interface simple : en quelques minutes, repartez avec une pizza chaude.</p>
<ul class="checks rv"><li><span><b>7 j/7, 24 h/24.</b></span></li><li><span><b>Des classiques</b> comme la Margherita ou la 4 fromages.</span></li><li><span><b>Et nos créations</b> originales.</span></li></ul></div>{tile(PH + 'p54.webp', '', par=8, alt='Un distributeur de pizzas Pizza des Lys')}</div></section>''' + cta('Et maintenant, <em>à table !</em>') + foot()

    opts = ''.join(f'<option value="{k}">{r["nom"]} · {r["ville"]}</option>' for k, r in R.items())
    cards = ''.join(f'<a class="rc rv" href="{PAGE[k]}"><span class="micro mute">{r["ville"]}</span><h3>{r["nom"]}</h3><p>{r["adr"]}</p><b>{r["tel"]}</b></a>' for k, r in R.items())
    cov = ''.join(f'<button type="button"{" class=on" if i == 2 else ""}>{i}</button>' for i in range(1, 9))
    P['reserver.html'] = head('Réserver une table ou une chambre — La Maison des Lys', 'Réservez votre table à Péronnas, Bourg-en-Bresse ou Châtillon-sur-Chalaronne, ou une chambre à l’Hôtel des Lys.', 'reserver.html') + pagehead('Réserver', 'Votre table <em>vous attend</em>', 'Choisissez votre restaurant, le jour, l’heure et le nombre de couverts. Ou réservez une chambre à l’Hôtel des Lys.', PH + 'p33.webp') + f'''
<section class="sec" id="reserver"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réservation en ligne</span><h2 class="sp">En <em>30 secondes</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Vous recevez une confirmation par e-mail. Pour un grand groupe, appelez directement le restaurant.</p></div>
<form class="f calc rv" id="resa"><div class="seg"><button type="button" class="on" data-m="table">Une table</button><button type="button" data-m="chambre">Une chambre</button></div>
<div class="fld mt"><label for="rr">Restaurant</label><select id="rr">{opts}</select></div>
<div class="r2"><div class="fld"><label for="rd">Arrivée</label><input id="rd" type="date" required></div><div class="fld mt"><label for="rh">Heure</label><select id="rh"><option>12 h 00</option><option>12 h 30</option><option>13 h 00</option><option>19 h 00</option><option>19 h 30</option><option>20 h 00</option><option>20 h 30</option><option>21 h 00</option></select></div><div class="fld mc" hidden><label for="rd2">Départ</label><input id="rd2" type="date"></div></div>
<div class="fld"><label class="mt">Couverts</label><label class="mc" hidden>Personnes</label><div class="cov">{cov}</div></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<div class="fld"><label for="re">E-mail</label><input id="re" type="email"></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Réserver</span><span>Réserver</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune réservation n’est envoyée.)</div></form></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Ou par téléphone</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3rem)">Nos <em>3 restaurants</em></h2><div class="rcs">{cards}</div></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
