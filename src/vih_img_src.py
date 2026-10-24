from pathlib import Path
SRC=Path(__file__).resolve().parent; ROOT=SRC.parent
# Builds data_vihimg.js: hero + described views for each mahāvihāra.
# Each view: k (image key), t (title), d (description), b (what it rests on: fact / trad / debated / interp), s (source keys)
import json
S={
'nal':['Nalanda mahavihara (Wikipedia, citing Xuanzang and Yijing)','https://en.wikipedia.org/wiki/Nalanda_mahavihara'],
'ietz':['Archaeological excavations at Nalanda (ASI findings)','https://www.indianetzone.com/76/archaeological_excavations_nalanda.htm'],
'dhs':['Dharmasvamin (Wikipedia)','https://en.wikipedia.org/wiki/Dharmasvamin'],
'xzm':['Xuanzang, Buddhist Records, tr. Beal – Magadha','https://www.wisdomlib.org/south-asia/book/buddhist-records-of-the-western-world-xuanzang/d/doc220246.html'],
'tax':['University of ancient Taxila (Wikipedia)','https://en.wikipedia.org/wiki/University_of_ancient_Taxila'],
'mjp':['Jakarta Post – Muarajambi’s monumental mystery','https://www.thejakartapost.com/news/2014/11/25/muarajambi-temple-jambi-s-monumental-mystery'],
'yij':['Yijing (Wikipedia)','https://en.wikipedia.org/wiki/I-tsing'],
'asiv':['ASI Excavation Branch Patna – Antichak','https://asiexbrpatna.bih.nic.in/antichak.htm'],
'vikb':['Banglapedia – Vikramashila Mahavihara','https://en.banglapedia.org/index.php/Vikramashila_Mahavihara'],
'vikw':['Vikramashila (Wikipedia)','https://en.wikipedia.org/wiki/Vikramasila'],
'jag':['Banglapedia – Jagaddala Mahavihara','https://en.banglapedia.org/index.php/Jagaddala_Mahavihara'],
'tel':['Telhara, Nalanda district (Wikipedia)','https://en.wikipedia.org/wiki/Telhara,_Nalanda_district'],
'telp':['The Peninsula / IANS – remains found in Bihar (2014)','https://thepeninsulaqatar.com/article/15/01/2014/another-ancient-varsity-s-remains-found-in-bihar'],
'lal':['Lalitagiri (Wikipedia, citing ASI 1985–91)','https://en.wikipedia.org/wiki/Lalitagiri'],
'lalu':['UNESCO Tentative List – Lalitgiri','https://whc.unesco.org/en/tentativelists/6926/'],
'lova':['Amusing Planet – The 1,600 pillars of Lovamahapaya','https://amusingplanet.com/2015/06/the-1600-stone-pillars-of-lovamahapaya.html'],
'ruw':['Ruwanwelisaya (Wikipedia)','https://en.wikipedia.org/wiki/Ruwanwelisaya'],
'mvs':['Sunday Times – the Mahāvaṃsa series','https://www.sundaytimes.lk/040307/funday/1.html'],
'abh':['Abhayagiri Vihāra (Wikipedia)','https://en.wikipedia.org/wiki/Abhayagiri_Vih%C4%81ra'],
'kut':['Kuttam Pokuna (Wikipedia)','https://en.wikipedia.org/wiki/Kuttam_Pokuna'],
'kan':['Kanheri Caves (Wikipedia)','https://en.wikipedia.org/wiki/Kanheri_Caves'],
'kani':['Puratattva – Kanheri inscriptions','https://puratattva.in/kanheri-inscriptions/'],
'nk':['Nagarjunakonda (Wikipedia)','https://en.wikipedia.org/wiki/Nagarjunakonda'],
'kcx':['Xuanzang, tr. Beal – Dravida / Kāñcīpura','https://www.wisdomlib.org/south-asia/book/buddhist-records-of-the-western-world-xuanzang/d/doc220264.html'],
'kcw':['Way of Bodhi – Buddhism in Kanchi','https://www.wayofbodhi.org/buddhism-in-kanchi-tamilnadu/'],
'valx':['Xuanzang, tr. Beal – Valabhī','https://www.wisdomlib.org/south-asia/book/buddhist-records-of-the-western-world-xuanzang/d/doc220274.html'],
'vald':['Deccan Herald – NIAS remote-sensing study of Valabhi (2025)','https://www.deccanherald.com/amp/story/india/gujarat/study-cites-remote-sensing-data-to-locate-ancient-valabhi-town-in-gujarat-3365811'],
'valb':['Britannica – Valabhi','https://www.britannica.com/place/Valabhi'],
'rat':['Ratnagiri, Odisha (Wikipedia, citing Mitra 1981–83)','https://en.wikipedia.org/wiki/Ratnagiri,_Odisha'],
'rata':['ASI/IGNCA report – Ratnagiri Monastery 1','https://ignca.gov.in/asi_reports/orjajpur065.pdf'],
'ratg':['GK Today – Ratnagiri excavations 2024–25','https://www.gktoday.in/ratnagiri-buddhist-excavations/'],
'sal':['Banglapedia – Shalvan Vihara','https://en.banglapedia.org/index.php/Shalvan_Vihara'],
'salu':['UNESCO Tentative List – Lalmai-Mainamati','https://whc.unesco.org/en/tentativelists/6670/'],
'od':['Odantapuri (Wikipedia)','https://en.wikipedia.org/wiki/Odantapuri'],
'odr':['Rajani and Kumar 2021, “Where Was Odantapuri Located?”, Resonance','https://eprints.iisc.ac.in/70565/'],
'som':['Banglapedia – Paharpur','https://en.banglapedia.org/index.php/Paharpur'],
'somw':['Somapura Mahavihara (Wikipedia)','https://en.wikipedia.org/wiki/Somapura_Mahavihara'],
'nat':['Nateshwar Deul (Wikipedia)','https://en.wikipedia.org/wiki/Nateshwar_Deul'],
'natd':['Daily Star – pyramid-shaped stupa at Nateshwar','https://www.thedailystar.net/city/news/pyramid-shaped-stupa-sheds-new-light-our-rich-past-1883179'],
'natp':['Prothom Alo – 1000-year-old Buddhist city in Munshiganj','https://en.prothomalo.com/science-technology/1000-yr-old-Buddhist-city-in-Munshiganj'],
}
V={}
def c(id,hero,views): V[id]={'hero':hero,'views':views}
def v(k,t,d,b,s): return {'k':k,'t':t,'d':d,'b':b,'s':s}

c('nalanda','nalanda_6',[
 v('nalanda_6','The campus at its height, c. 9th century',"A long row of eleven brick monasteries on the east faces a line of great temples on the west, with a broad walkway between them, as the excavated plan shows. Each monastery is a square of monks’ cells around an open court with a shrine facing the entrance. Pilgrims and monks fill the walkway. The layout follows the ASI plan; the upper storeys and roofs are reconstructed.",'fact',['ietz','nal']),
 v('nalanda_2','The entrance test at the gate, c. 640 CE',"A senior scholar questions a nervous young monk at the main gateway while applicants from other lands, including a Chinese monk, wait their turn. Xuanzang wrote that the gatekeepers examined everyone who wished to enter, and that most applicants failed and turned away. The gateway and walls are reconstructed.",'trad',['nal']),
 v('nalanda_8','A day at Nālandā, c. 680 CE',"Monks bathe and wash their robes at a large brick-lined tank, a bell is struck, and a water clock floats in a basin to mark the hours. Yijing, who lived here for about ten years, described bathing at the tanks and the regulated hours of monastic life. The water clock should be checked against a translation of Yijing before being treated as fact.",'trad',['nal','yij']),
 v('nalanda_10','Temple 3, the great stupa temple',"The largest temple on the site, built up in at least seven successive phases. The fifth phase is best preserved, with four corner towers, and its towers and stair-sides carry Gupta-period stucco panels of Buddhas and Bodhisattvas. Small votive stupas cluster at its base. Its upper levels are reconstructed.",'fact',['ietz']),
 v('nalanda_3','Temple 2 and its carved base',"The base of Temple 2 is lined with a continuous row of 211 sculpted stone panels, the feature that makes this temple stand out in the ASI record. A sculptor and a monk examine a panel. Only the decorated base survives; the brick temple above it is reconstructed.",'fact',['ietz']),
 v('nalanda_1','The colossal Buddha of Temple 14',"An enormous seated Buddha fills the dim sanctum of Temple 14. The ASI found the remains of a huge image here, and the front of its pedestal carries the only surviving mural painting at Nālandā, shown here in red, ochre and black. Monks sit in meditation by lamplight.",'fact',['ietz']),
 v('nalanda_4','Monastery 1 and the Śrīvijaya king’s gift, 9th century',"Monastery 1 is the oldest and most important monastery on the site, rebuilt on as many as nine levels. Its lower monastery is linked to Bālaputradeva, king of Śrīvijaya in Sumatra, during the reign of the Pāla king Devapāla. Here envoys present a copper-plate charter in the courtyard, before a colossal seated Buddha.",'fact',['ietz','nal']),
 v('nalanda_11','Casting bronzes beside Temple 13',"Beside Temple 13 the ASI found a brick smelting furnace with four chambers, along with burnt metal and slag that point to metal casting. Artisans pour molten bronze while finished small images cool on a mat. The scene of the workshop at work is reconstructed from those finds.",'fact',['ietz']),
 v('nalanda_5','The colossal Buddha of the Sarai temple',"A towering standing Buddha inside the great Sarai temple, the tallest building of the campus. The figure and its scale are a reconstruction drawn from the remains at the Sarai mound; its exact height is an estimate.",'interp',['nal']),
 v('nalanda_9','Section through the Sarai temple',"A cut-away drawing showing the colossal Buddha standing in the inner sanctum, with a covered walkway around it and a column of monks for scale. The height shown is an estimate used to give a sense of the image’s size, not a measured figure.",'interp',['nal']),
 v('nalanda_7','Dharmasvāmin’s visit, c. 1235 CE',"After the raids, the Tibetan pilgrim Dharmasvāmin found most of Nālandā’s monasteries abandoned, with only two still in use. The ninety-year-old abbot Rāhula Śrībhadra still taught grammar to about seventy students, and monks sometimes hid in the forest when raiders came. Here the old master teaches in a ruined courtyard while Dharmasvāmin takes notes.",'trad',['dhs']),
])
c('taxila','taxila_1',[
 v('taxila_1','Jauliāṇ monastery above Taxila, 2nd–5th century',"The hilltop monastery of Jauliāṇ: an upper court crowded with small votive stupas and Buddha figures, and a lower court of monks’ cells on two storeys around a square tank. The walls of Sirkap city lie in the valley beyond. The plan follows the excavated remains; the upper floors and finishes are reconstructed.",'fact',['tax']),
 v('taxila_3','Inside Jauliāṇ: the healing Buddha',"Monks study around the courtyard tank while a pilgrim touches a seated Buddha. One of Jauliāṇ’s Buddhas has a small hole in its navel where pilgrims are said to have placed a finger to pray for healing, and statue bases here carry donor inscriptions in Kharoṣṭhī script.",'trad',['tax']),
 v('taxila_4','Dharmarājikā stupa',"The great round stupa of Taxila, linked by tradition to relics distributed by Aśoka. A ring of small chapels and votive stupas surrounds it, and pilgrims walk clockwise around its base. The ring of chapels and the stupa base survive; the dome and umbrella stack are reconstructed.",'trad',['tax']),
 v('taxila_2','Xuanzang at the ruins, c. 630 CE',"A lone Chinese pilgrim with a frame of scrolls on his back looks down on broken walls and collapsed stupas. When Xuanzang passed through Taxila, he found its monasteries largely deserted and ruined after the invasions of the late 5th century.",'trad',['tax']),
])
c('muarajambi','muarajambi_4',[
 v('muarajambi_4','Temples along the Batang Hari, c. 11th century',"Walled brick temple compounds spread along the north bank of the Batang Hari river, separated by forest and joined by canals. The real site stretches for several kilometres, and its temples stand on raised ground above the floods. Malay trading ships with tilted mat sails pass on the river.",'fact',['mjp']),
 v('muarajambi_2','Yijing arrives at the river port, c. 680 CE',"The Chinese monk Yijing steps off a trading ship at a wooden jetty and is greeted by local monks. Yijing wrote that more than a thousand monks studied in the Śrīvijaya capital and advised Chinese monks to stay there a year or two before going on to India. Whether his city was at Muara Jambi or Palembang is debated.",'debated',['yij']),
 v('muarajambi_7','Atiśa studies with Serlingpa, c. 1015 CE',"The Sumatran master Dharmakīrti, known in Tibet as Serlingpa, teaches the young Bengali monk Atiśa in a timber pavilion beside a brick temple. Tibetan sources say Atiśa spent about twelve years with him in Suvarṇadvīpa. Linking that teacher to Muara Jambi specifically is a strong tradition but not proven.",'debated',['mjp']),
 v('muarajambi_6','Installing the Prajñāpāramitā at Candi Gumpung',"Monks raise a white andesite statue of Prajñāpāramitā, the goddess of the Perfection of Wisdom, onto her pedestal while lay people bring lotus flowers. Her hands are in the teaching gesture, dharmachakra mudrā. The statue was found at Candi Gumpung and is dated to the 13th century.",'fact',['mjp']),
 v('muarajambi_5','Canals and brick-makers, c. 11th century',"Boats loaded with fresh bricks and ceramic jars move along a man-made canal between temple enclosures, while workers shape and fire bricks on the bank. Canals running from the Batang Hari are part of the excavated landscape; the scene of daily work is reconstructed.",'fact',['mjp']),
 v('muarajambi_1','Candi Kedaton, the largest enclosure',"Candi Kedaton is the largest temple compound at Muara Jambi, about five hectares inside its walls. Monks cook for the monastery in a large bronze pot, like the one found near the site, and a stone guardian stands at the gate.",'fact',['mjp']),
 v('muarajambi_3','Studying before the Prajñāpāramitā',"Monks read palm-leaf manuscripts in an open pavilion before a crowned image of Prajñāpāramitā with her hands in the teaching gesture. Lotus and jasmine offerings rest in a bronze bowl. A reconstruction of study at the monastery, built around the statue found at Candi Gumpung.",'interp',['mjp','yij']),
])
c('vikramashila','vikramashila_6',[
 v('vikramashila_6','The great square monastery, c. 10th century',"A vast square monastery about 330 m on each side, with 208 cells facing an inner verandah, and a cross-shaped temple at its centre. The main gate is on the north, toward the Ganga. All of this follows the ASI excavation; the building above the excavated walls is reconstructed.",'fact',['asiv','vikb']),
 v('vikramashila_5','The north gate and a gate scholar',"A senior scholar questions a newly arrived monk at the north gate, where clusters of votive stupas stand on either side. Tibetan tradition, recorded by Tāranātha, says each of Vikramaśīla’s six gates was guarded by a scholar who tested newcomers. The gate and stupas follow the excavation; the gate scholars are tradition.",'trad',['vikb','asiv']),
 v('vikramashila_1','The central cross-shaped temple',"The brick temple at the centre of the courtyard, built in two terraces with walkways about 2.9 m wide and a chamber facing each of the four directions. The ASI found that these chambers once held colossal clay images of the Buddha and Bodhisattvas.",'fact',['asiv','vikb']),
 v('vikramashila_3','Inside a monk’s cell',"A square brick cell about 4 m across, with a narrow doorway and a raised bed-platform about 3 by 2 m, as Banglapedia records. A monk reads a palm-leaf manuscript by lamplight, with a small bronze Buddha in a wall niche.",'fact',['vikb']),
 v('vikramashila_4','The manuscript house',"A long building in the south-west corner, about 41.5 by 18.65 m, with thirteen narrow vents in its thick south wall. Scholars think the vents and a reservoir beside it kept the air cool to protect manuscripts. The ASI calls it the presumed library, so its use is not certain.",'debated',['vikb','vikw']),
 v('vikramashila_7','Atiśa leaves for Tibet, c. 1040 CE',"The elderly Bengali master Atiśa, head of Vikramaśīla, leaves for Tibet with the Tibetan translator Nagtso and a train of manuscripts, while the monks gather to say farewell. His journey is recorded in Tibetan biographies.",'trad',['vikb']),
 v('vikramashila_2','Fire and abandonment, c. 1206 CE',"Blackened cells, collapsed roofs and scattered fragments after a great fire. Ash layers found in the cells suggest the monastery burned, and the ASI dates its destruction to about 1206. Villagers carry off bricks; a later fort nearby was built from material robbed from the monastery.",'fact',['asiv','vikb']),
])
c('jagaddala','jagaddala_2',[
 v('jagaddala_2','The monastery and its east gate, c. 1100 CE',"The monastery seen from the east gate, with its unusual semicircular corner towers, bands of terracotta plaques and ornamental brick, and two inscribed stone pillars at the entrance. Monks study on the verandah around the courtyard. The excavation of 1996 exposed only part of the monastery; the rest is reconstructed.",'fact',['jag']),
 v('jagaddala_4','Scholars from Vikramaśīla take refuge',"Monks carrying bundles of manuscripts arrive at the east gate by bullock cart and are welcomed inside. Banglapedia records that scholars from Vikramaśīla, including Śubhākaragupta and Abhayākaragupta, are believed to have taken shelter at Jagaddala and written many works here.",'trad',['jag']),
 v('jagaddala_6','Carving the gate inscription',"A scribe chisels a short inscription into an octagonal stone pillar. Two such pillars were found, one near the eastern gateway naming the writer Śrī Makkaḍa Nandi of Gaṅgāpura, and both are dated by their proto-Bengali script to about the 12th–13th century.",'fact',['jag']),
 v('jagaddala_5','The terracotta wall',"An artisan fits a plaque into the western outer wall. Plaques showing a doorkeeper, an archer, deer and birds were found still in place on this wall, alongside ornamental bricks with lotus-petal, chain and zigzag designs.",'fact',['jag']),
 v('jagaddala_1','A cell with its stone altar',"A monk translates a Sanskrit manuscript while a Tibetan monk writes it out in Tibetan. Several excavated cells had stone altars for images, and Avalokiteśvara is named as the monastery’s presiding deity. Many Tibetan translations of Vajrayāna texts are thought to have been made here.",'fact',['jag']),
 v('jagaddala_3','Vidyākara compiles his anthology',"An elderly scholar chooses verses while a young monk copies them onto palm leaves. Vidyākara, a scholar of Jagaddala, compiled the Subhāṣitaratnakośa, a large anthology of Sanskrit poetry.",'trad',['jag']),
])
c('telhara','telhara_4',[
 v('telhara_4','Tilāḍhaka as Xuanzang described it, c. 637 CE',"Xuanzang describes Tilāḍhaka as having four halls with three-storey pavilions, high towers and double gates, and about a thousand monks studying the Mahāyāna. He places three shrines on the road facing the middle gate. The building plan here is a reconstruction based on his account.",'trad',['xzm','tel']),
 v('telhara_1','The three shrines: Buddha, Tārā and Avalokiteśvara',"Xuanzang records three vihāras on the road facing the middle gate. The central one held a standing Buddha about thirty feet high, with Tārā on the left and Avalokiteśvara on the right, crowned with metal rings and bells. He says the images were made of a metallic stone. Statues of Avalokiteśvara and Maitreya from Telhāra are now in the Indian Museum, Kolkata.",'trad',['xzm','tel']),
 v('telhara_5','A Mahāyāna lecture',"Hundreds of monks listen to a teacher in the courtyard of a three-storey hall, with a Chinese pilgrim among them. Xuanzang names the chief monk as Prajñābhadra and says about a thousand monks lived here, studying the Mahāyāna.",'trad',['xzm','tel']),
 v('telhara_2','Sealing letters with clay seals',"A monk presses a seal into wet clay that closes the cord around a bundle of palm-leaf letters, with finished sealings drying on a ledge. More than a hundred seals have been found in the excavations at Telhāra.",'fact',['telp']),
 v('telhara_3','The excavation today',"Archaeologists work in trenches across the mound, recording brick walls, pottery and small finds. Excavation at Telhāra began in 2009, and the Bihar Heritage Development Society dug again in 2020–22, uncovering a three-storey structure, prayer halls and residential cells.",'fact',['tel','telp']),
])
c('lalitgiri','lalitgiri_4',[
 v('lalitgiri_4','The great monastery, 10th–11th century',"The largest of Lalitgiri’s four monasteries: two storeys, about 36 m square, around an open court about 12.9 m across, with a brick rainwater cistern at the rear. The relic stupa and chaitya hall stand on the hill behind. The plan follows the ASI excavation of 1985–91.",'fact',['lal']),
 v('lalitgiri_1','The nested relic caskets',"The first Buddha relics found in eastern India: an outer casket of khondalite stone shaped like a small stupa, holding smaller boxes of steatite, silver and gold, one inside the next. The innermost gold box held a small piece of bone. Two such deposits were found in the main stupa.",'fact',['lal','lalu']),
 v('lalitgiri_2','The apsidal chaitya hall',"A long east-facing brick hall, 33 by 11 m, with walls 3.3 m thick and a circular stupa at its rounded far end. It is the first structure of this kind found in Odisha. Kushan-period Dhamma Lipi inscriptions were found around it.",'fact',['lal']),
 v('lalitgiri_3','The stupa in the apse',"A closer view of the circular stupa inside the chaitya hall, ringed by a stone railing carved with half-lotus medallions, like the railing fragment found at the site. Monks walk around it with lamps and flowers.",'fact',['lal']),
 v('lalitgiri_6','A sanctum with Mahāyāna images',"A colossal grey stone Buddha touching the earth, flanked by Bodhisattva figures. One monastery had large Buddha heads in its sanctum, and the site has yielded many Mahāyāna sculptures of the Buddha, Bodhisattvas, Tārā and Jambhala carved in khondalite.",'fact',['lal','lalu']),
 v('lalitgiri_5','The Chandrāditya Vihāra seal',"A monk seals palm-leaf letters with the monastery’s seal. A terracotta sealing found here, dated to the 9th–10th century, reads “Śrī Chandrāditya Vihāra Samagra Ārya Bhikṣu Saṅghasa”: of the whole community of noble monks of the Śrī Chandrāditya Vihāra.",'fact',['lal','lalu']),
])
c('mahavihara','mahavihara_3',[
 v('mahavihara_3','The Lovamahāpāya, the Brazen Palace',"A huge monastic hall standing on a grid of 40 by 40 granite pillars, 1,600 in all, roofed with copper-bronze plates. The Mahāvaṃsa says it rose nine storeys with a thousand rooms on each floor, which scholars treat as exaggerated. Only the stone pillars survive today.",'trad',['lova','mvs']),
 v('mahavihara_2','Planting the Bodhi tree, 3rd century BCE',"The nun Saṅghamittā and King Devānaṃpiya Tissa water a young fig tree on a stone terrace. By tradition the Sri Mahā Bodhi grew from a cutting of the Bodh Gayā tree that Saṅghamittā brought to Sri Lanka.",'trad',['mvs']),
 v('mahavihara_1','Building the Ruwanwelisāya, c. 140 BCE',"Workers, elephants and scaffolding raise the great dome while King Duṭṭhagāmaṇī watches. The original stupa was about 55 m high; it has since been rebuilt to about 103 m.",'fact',['ruw']),
 v('mahavihara_4','Sealing the relic chamber',"Two young novices lower a stone block over the relic chamber while senior monks chant. The Mahāvaṃsa says the relics were enshrined in a golden Buddha image and that the chamber was closed by the novices Uttara and Sumana.",'trad',['ruw','mvs']),
 v('mahavihara_5','Buddhaghosa writes the commentaries, 5th century',"The Indian monk Buddhaghosa writes Pali on palm leaves while Sri Lankan elders check his work. He wrote the Visuddhimagga and Pali commentaries at the Mahāvihāra, and these works survive.",'fact',['mvs']),
])
c('abhayagiri','abhayagiri_intro',[
 v('abhayagiri_intro','Abhayagiri monastery',"The brick-red Abhayagiri stupa rises above halls, bathing ponds and a carved moonstone at the foot of a stair, with monks studying in the pavilions. A green-stone Buddha in one hall recalls the jade image Faxian described; its details are not confirmed.",'interp',['abh']),
 v('abhayagiri_1','Founding the stupa, 89 BCE',"King Vaṭṭagāmaṇī Abhaya watches workers lay the first brick courses of a great round stupa. He founded Abhayagiri after defeating the last Tamil king in 89 BCE, on the site of an earlier hermitage.",'fact',['abh']),
 v('abhayagiri_2','The tooth relic procession, 412 CE',"The Buddha’s tooth relic is carried on an elephant toward Abhayagiri, along a road lined with painted scenes of the Buddha’s past lives. Faxian, who watched it in 412 CE, described exactly this display; he is shown at the left in grey robes.",'trad',['abh']),
 v('abhayagiri_4','Kuttam Pokuna, the twin ponds',"Two stepped bathing ponds of dressed granite: the southern one 40 by 16 m and 5.5 m deep, the northern one 28 by 16 m and 4.3 m deep. Water reached them through underground channels and a filter, entering beneath a carved five-hooded cobra.",'fact',['kut']),
 v('abhayagiri_5','The Ratnaprāsāda and its guard stone',"Granite steps rise to a pillared hall, with a carved moonstone at their foot and a guard stone showing a cobra king beside them. The guard stone found at the Ratnaprāsāda is regarded as one of the finest ever discovered.",'fact',['abh']),
 v('abhayagiri_3','Monks studying both teachings',"Monks read palm-leaf manuscripts in a pillared hall with a seated Buddha and a standing Avalokiteśvara. Xuanzang described Abhayagiri’s monks as studying both the early teachings and the Mahāyāna, and Avalokiteśvara is still honoured in Sri Lanka as Nātha.",'trad',['abh']),
])
c('kanheri','kanheri_intro',[
 v('kanheri_intro','The caves of Kanheri',"Over a hundred rock-cut caves carved into a basalt hillside near Mumbai, linked by stairs and fed by rainwater channels. The great chaitya façade with its colossal Buddhas stands at the centre, and the Arabian Sea is visible beyond.",'fact',['kan']),
 v('kanheri_1','Inside the Great Chaitya (Cave 3)',"A rock-cut prayer hall about 26 m long, with 34 pillars around the nave and a stupa nearly 5 m across at the rounded far end. An inscription of the Sātavāhana king Yajña Śrī Sātakarṇi, about 170 CE, is carved on the verandah.",'fact',['kan']),
 v('kanheri_5','The verandah and its colossal Buddhas',"Two standing Buddhas about 7 m tall are carved at either end of the chaitya verandah. They were added considerably later than the cave itself. The carved screen between them holds some of the site’s finest figures.",'fact',['kan']),
 v('kanheri_4','Cells, stairs and cisterns',"Monsoon rain runs along channels cut into the rock and fills square cisterns in front of the caves. Most caves at Kanheri have their own cistern and a stone bed-platform inside.",'fact',['kan']),
 v('kanheri_6','A merchant couple gives a cave',"A merchant couple from the port of Sopara dedicate a cave while a stonecutter carves the donation record. Kanheri’s inscriptions record gifts of caves, cisterns, benches and endowments, mostly from merchants, goldsmiths, monks and nuns of Kalyāṇa and Sopara.",'fact',['kani']),
 v('kanheri_2','The Avalokiteśvara litany',"A carved panel with a large Avalokiteśvara at its centre and small scenes of him saving devotees from dangers such as shipwreck and fire. A woman lights a lamp before it. Avalokiteśvara is the most distinctive figure at Kanheri.",'fact',['kan']),
])
c('nagarjunakonda','nagarjunakonda_intro',[
 v('nagarjunakonda_intro','Queen Chāṃtisiri’s offering',"Queen Chāṃtisiri of the Ikṣvāku family makes an offering at the Mahāchaitya, attended by monks and women of the court. Inscriptions record that she renovated the great stupa and funded it for ten years. The site’s ancient name was Vijayapurī.",'fact',['nk']),
 v('nagarjunakonda_2','The Mahāchaitya and its pillars',"The great stupa, about 32 m across and 18 m high with a 4 m walkway, its plastered dome decorated with a garland band. Tall stone pillars stand on platforms around it. The stupa is believed to hold relics of the Buddha.",'fact',['nk']),
 v('nagarjunakonda_3','Vijayapurī, the Ikṣvāku capital',"A fortified city beside the Krishna river, with dozens of monasteries spread across the valley. At its peak this was the largest Buddhist centre in South India, with more than thirty monasteries.",'fact',['nk']),
 v('nagarjunakonda_1','Cūḷadhammagiri, the monastery for Sri Lankan monks',"A brick monastery with cells, a small stupa and a chaitya hall on a hill. Inscriptions record monasteries here for monks of the Sri Lankan Mahāvihāra school, including one for scholars from Ceylon.",'fact',['nk']),
 v('nagarjunakonda_6','Carving the limestone reliefs',"Sculptors carve pale limestone panels of the Buddha’s life in the style of nearby Amarāvatī. The reliefs of Vijayapurī closely resemble the final phase of the Amarāvatī stupa.",'fact',['nk']),
 v('nagarjunakonda_5','Saving the site before the dam, 1954–60',"Archaeologists dismantle and number monuments before the Nāgārjuna Sagar dam floods the valley. Some were rebuilt on top of Nāgārjuna’s hill, now an island with a museum opened in 1966; others were moved to the mainland.",'fact',['nk']),
])
c('kanchi','kanchi_intro',[
 v('kanchi_intro','The Aśoka stupa outside Kāñcīpura',"A great white stupa about 30 m high in a walled monastery south of the city. Xuanzang counted about a hundred monasteries and 10,000 monks at Kāñcī and described a stupa about 100 feet high built by Aśoka. The monasteries themselves have never been excavated.",'trad',['kcx']),
 v('kanchi_2','Xuanzang arrives at Kāñcī, c. 640 CE',"The Chinese pilgrim, with his frame of scrolls, is welcomed by Tamil monks and townspeople. Xuanzang wrote that the people of the region were brave, honest and valued learning.",'trad',['kcx']),
 v('kanchi_6','Dharmapāla leaves for Nālandā',"A young monk sets off north along the road while his teacher and fellow monks bless him from the roadside. Xuanzang records that Kāñcīpura was the native place of Dharmapāla, who later became head of Nālandā.",'trad',['kcx']),
 v('kanchi_4','Worship before a standing Buddha',"Devotees offer jasmine before a tall standing Buddha. A standing Buddha about 2.4 m high was found at the Kāmākṣī temple in Kāñcīpura and is now in the Chennai Museum.",'fact',['kcw']),
 v('kanchi_1','Maṇimēkalai and her teacher',"The young nun Maṇimēkalai sits with the Buddhist teacher Aravaṇa Aṭikaḷ in a monastery garden. In the Tamil epic Maṇimēkalai, he guides her onto the Buddhist path at Kāñcī.",'trad',['kcw']),
 v('kanchi_7','A seated Buddha shrine, 11th century',"Monks chant before a seated granite Buddha in meditation. Several seated Buddhas of the 10th–12th centuries have been found in and around Kāñcīpura, in temple compounds, at a school and at a police station.",'fact',['kcw']),
 v('kanchi_3','A Buddha carved on a pillar',"A mason carves a small seated Buddha into a granite pillar. Pillars carved with Buddha images survive at the Kachapeshwarar temple in Kāñcīpura; who carved them and why is not recorded.",'fact',['kcw']),
])
c('valabhi','valabhi_intro',[
 v('valabhi_intro','The Maitraka capital',"A walled palace mound inside a moat fed by two branches of the Ghelo river, with the city and its monasteries spread around it. A 2025 satellite study by NIAS Bengaluru traced this layout under the modern town of Vallabhipur; it has not been excavated.",'fact',['vald']),
 v('valabhi_5','King Dhruvapaṭa’s assembly',"The king stands and offers robes to seated monks during a great assembly. Xuanzang wrote that King Dhruvapaṭa held a seven-day assembly every year, giving the monks robes, medicines and gems.",'trad',['valx']),
 v('valabhi_2','The great monastery of Ācāra',"A two-storey brick monastery outside the city, with monks of the Sammitīya school walking with alms bowls. Xuanzang counted about a hundred monasteries and 6,000 monks at Valabhī and described a great monastery near the city built by the arhat Ācāra.",'trad',['valx']),
 v('valabhi_1','Sthiramati writing',"An elderly scholar writes on palm leaves while young monks copy. Xuanzang says the Bodhisattvas Sthiramati and Guṇamati lived at Valabhī and wrote widely known treatises.",'trad',['valx']),
 v('valabhi_4','A copper-plate grant',"A royal officer hands copper plates to an abbot, granting land to support the monks. Maitraka copper-plate grants and seals have been found at Vala, the modern village on the site.",'fact',['valb']),
 v('valabhi_3','The harbour',"Ships unload cloth and other goods beside brick warehouses while a monk receives a merchant’s gift. Xuanzang described Valabhī as very wealthy, with rare goods from distant lands stored there in great quantities.",'trad',['valx']),
])
c('ratnagiri','ratnagiri_intro',[
 v('ratnagiri_intro','Ratnagiri Mahāvihāra, c. 10th century',"The main stupa on its square base surrounded by hundreds of small votive stupas, with Monastery 1 below it. The ASI found more than 700 votive stupas here, and Monastery 1 is about 55 m square with at least two storeys.",'fact',['rat','rata']),
 v('ratnagiri_3','The chlorite doorway of Monastery 1',"A monk passes through the richly carved doorway of dark green chlorite stone, described as the loveliest entrance to a structural monastery in India. Its jambs carry small Buddhas, guardian figures and river goddesses.",'fact',['rat']),
 v('ratnagiri_4','The great Buddha of Monastery 1',"A colossal seated Buddha touching the earth fills the shrine opposite the entrance, flanked by standing Bodhisattvas. The ASI report gives the image as 2.15 m high.",'fact',['rata']),
 v('ratnagiri_1','The monastery’s seals',"A monk presses seals into clay. The excavation found 1,386 clay seals, most reading “Śrī Ratnagiri Mahāvihārīya Ārya Bhikṣu Saṅghasya”, which identified the monastery by name.",'fact',['rat']),
 v('ratnagiri_2','Teaching the Kālacakra, 10th century',"A Vajrayāna master teaches monks, some of them Tibetan, beside a carved deity. A Tibetan history names Ratnagiri as a centre of Kālacakra teaching in the 10th century; the link is still debated.",'debated',['rat']),
 v('ratnagiri_6','The ASI excavation of 2024–25',"Archaeologists uncover a colossal stone Buddha head and a huge carved palm. The ASI resumed digging here after sixty years and also found inscribed relics of the 8th–9th centuries.",'fact',['ratg']),
])
c('shalban','shalban_intro',[
 v('shalban_intro','Śrī Bhavadeva Mahāvihāra, c. 8th century',"A square monastery 167.6 m on each side on the Lalmai ridge, with a single gateway in the north wing, a 5 m thick back wall, and a cross-shaped shrine in the courtyard. Seals give its original name, Śrī Bhavadeva Mahāvihāra.",'fact',['sal','salu']),
 v('shalban_5','The cross-shaped shrine',"Monks walk around the terraced central shrine. Its Period III cross-shaped form, about 51.8 m long, had terracotta plaques set in ornamental brick bands around its base, closely resembling Paharpur.",'fact',['sal']),
 v('shalban_4','King Bhavadeva founds the monastery',"The king offers copper plates to the monks as the monastery walls rise. It was founded by Śrī Bhavadeva, fourth ruler of the early Deva dynasty, around the end of the 7th or start of the 8th century.",'fact',['sal','salu']),
 v('shalban_2','Life in a cell',"A monk reads in a small brick cell with three stepped niches in its walls and a fireplace in the corner. Each excavated cell has three corbelled niches, and fireplaces and brick pedestals were added in later phases.",'fact',['sal']),
 v('shalban_1','The treasury',"A monk and a steward count coins beside copper plates on a ring and clay sealings. The finds here include seven or eight copper-plate grants and between 350 and 400 gold, silver and copper coins.",'fact',['sal','salu']),
])
c('odantapuri','odantapuri_intro',[
 v('odantapuri_intro','Odantapurī as it may have looked',"A vast walled monastery with a terraced cross-shaped temple at its centre. Odantapurī has not been excavated and its site is debated. This plan follows its sister monasteries, Vikramaśīla and Somapura, and a large buried structure at Begampur near Nālandā identified by satellite study.",'debated',['od','odr']),
 v('odantapuri_1','A great assembly',"Thousands of monks fill the courtyard around the central temple. Tāranātha wrote that about a thousand monks lived here permanently and that occasionally as many as twelve thousand gathered.",'trad',['od']),
 v('odantapuri_3','Tibetan builders study the plan',"Tibetan monks measure the temple and draw its plan, guided by Indian monks. Tibetan sources say Samye, Tibet’s first monastery, was modelled on Odantapurī.",'trad',['od']),
 v('odantapuri_5','A shrine with Pāla images',"Monks make offerings before a polished black basalt Buddha in the Pāla style. A small brass image of Queen Māyā found at Bihar Sharif carries an inscription naming Uddaṇḍapura, the old name of Odantapurī.",'fact',['od']),
 v('odantapuri_2','The “fortress” that was a monastery, c. 1200',"Mounted soldiers halt before high brick walls. The Persian historian Minhāj-i-Sirāj describes a raid on a fortified place called Bihar that turned out to be a college. Whether he meant Odantapurī or Nālandā is debated.",'debated',['od']),
])
c('somapura','somapura_intro',[
 v('somapura_intro','Somapura Mahāvihāra, c. 9th century',"A square monastery about 274 m on each side with 177 cells, the main gateway on the north, and a cross-shaped temple on three terraces about 24 m high. The refectory and kitchen stand in the eastern part of the courtyard. It is a UNESCO World Heritage Site.",'fact',['som','somw']),
 v('somapura_2','The temple from the courtyard',"Looking up at the central temple rising in three terraces with stairs and projecting chapels. About 21 m of its original 24 m height survives.",'fact',['som']),
 v('somapura_3','Walking the terrace',"A monk walks the terrace beside bands of terracotta plaques. More than 2,000 plaques still decorate the walls, and 63 stone reliefs are set into the base. The relief shown is Padmapāṇi, the only Buddhist image among them.",'fact',['som']),
 v('somapura_4','The view from a cell',"From a small cell about 4 m square, the doorway frames the central temple across the courtyard. Each of the 177 cells measures about 4.26 by 4.11 m.",'fact',['som']),
 v('somapura_6','A festival of lamps',"Lamps line every terrace of the temple and the verandah of the cells. The plan of the temple and monastery follows the excavation; the festival itself is an artistic impression.",'interp',['som']),
 v('somapura_7','Cut-away of the central temple',"A labelled cut-away showing the three terraces and their walkways, the chapels on the upper terrace and the hollow central shaft. The upper parts are lost and the summit is conjectural; check the shaft detail against Dikshit’s excavation report.",'interp',['som']),
 v('somapura_1','A Javanese monk sketches the plan',"A monk from Java sketches the cross-shaped plan from the top terrace. Scholars compare Somapura’s temple to Buddhist temples in Myanmar, Java and Cambodia, naming Chandi Sewu as the closest. This visit is an artistic interpretation, not a recorded event.",'interp',['somw']),
])
c('vikrampur','vikrampur_intro',[
 v('vikrampur_intro','The pyramid stupa of Nateshwar',"A stepped, pyramid-shaped brick stupa about 44 m square, the only one of its kind found in Bangladesh. Carbon-14 dating places it at 780–950 CE, before Atiśa was born in this region.",'fact',['natd','nat']),
 v('vikrampur_2','Four linked stupas',"A group of four stupas joined on one platform, with a small pillared hall beside it. Excavators found such four-stupa groups, octagonal stupas, brick roads, a thick boundary wall and a northern gate at Nateshwar.",'fact',['nat','natd']),
 v('vikrampur_3','Atiśa as a young man',"A young prince-scholar walks with his teacher among the stupas of Bikrampur. Atiśa was born in this region in 982 and was a lay prince before he became a monk. The link between him and these particular monuments is speculative.",'debated',['nat']),
 v('vikrampur_1','Building with volcanic-ash mortar',"Workers mix grey mortar while a monk checks a wall with a plumb line. Excavators report that the builders used pumicite, a volcanic ash, which helps protect against humidity.",'fact',['nat']),
 v('vikrampur_4','The kitchen and the coin hoard',"Monks cook rice in large earthenware pots while one counts red and black copper coins. A deposit of such coins, along with cooking pots, water pots and lamps, was found at the site.",'fact',['nat']),
 v('vikrampur_6','The excavation today',"Archaeologists record trenches across the stupa terraces. Bangladeshi teams from Jahangirnagar University have dug here since 2012–13, joined by a Chinese archaeological institute in 2014, with support from the Agrashar Bikrampur Foundation.",'fact',['nat','natp']),
])
RW=json.load(open(SRC/'vih_rewrite.json',encoding='utf-8'))
for _id,_v in V.items():
  for _x in _v['views']:
    if _x['k'] in RW: _x['t'],_x['d']=RW[_x['k']][0],RW[_x['k']][1]
out={'S':S,'V':V}
js='window.VIH_IMG='+json.dumps(out,ensure_ascii=False)+';'
open(ROOT/'data_vihimg.js','w',encoding='utf-8').write(js)
print(sum(len(x['views']) for x in V.values()), len(V))
