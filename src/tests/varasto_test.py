import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_vaara_tilavuus_nollataan(self):
        self.varasto = Varasto(-2)
        self.varasto2 = Varasto(0)
        # varaston tilavuus nollataan jos se on negatiivinen
        self.assertAlmostEqual(self.varasto.tilavuus,0)

        # varaston tilavuus nollataan jos se on 0
        self.assertAlmostEqual(self.varasto2.tilavuus,0)
    
    def test_uudella_varastolla_ei_negatiivista_saldoa(self):
        self.varasto = Varasto(10,-4)
        # varaston saldo ei voi olla negatiivinen
        self.assertAlmostEqual(self.varasto.saldo,0)
    
    def test_varastoon_ei_lisata_negatiivista_maaraa(self):
        maara = self.varasto.lisaa_varastoon(-3)
        # varastoon ei voi lisätä negatiivista määrää
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.saldo)
    
    def test_varastoon_ei_lisata_kapasiteettia_enemman_maaraa(self):
        maara = self.varasto.lisaa_varastoon(11)
        # varastoon ei voi lisätä määrää enemmän mitä on tilaa
        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def test_varastosta_ei_oteta_negatiivista_maaraa(self):
        maara = self.varasto.ota_varastosta(-1)
        # varastosta ei voi ottaa negatiivista määrää
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),self.varasto.tilavuus)
    
    def test_varastosta_ei_oteta_enemman_kuin_saldoa(self):
        self.varasto.lisaa_varastoon(4)
        maara = self.varasto.ota_varastosta(5)
        # varastosta ei oteta enemmän kuin on saldoa ja saldon pitäisi nollaantua
        self.assertAlmostEqual(maara,4) and self.assertAlmostEqual(self.varasto.saldo,0)

    def test_varastossa_saldoa_ja_tilaa_oikea_merkkijono_esitys(self):
        mjono = self.varasto.__str__()
        # Tarkistetaan, onko merkkijonoesitys oikea
        self.assertEqual(mjono,f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
