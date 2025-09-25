import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class ModemFinanceAnalyzer:
    def __init__(self):
        self.parti = "Mouvement Démocrate (MoDem)"
        self.colors = ['#FF9900', '#FFCC00', '#FF6600', '#CC9900', '#FF9933', 
                      '#CC6600', '#FFCC33', '#FF9966', '#CC9933', '#FFCC66']
        
        self.start_year = 2007  # Création du MoDem
        self.end_year = 2025
        self.creation_year = 2007
        self.udi_creation = 2012  # Création de l'UDI (concurrent)
        
        # Configuration spécifique au MoDem
        self.config = {
            "type": "parti_politique",
            "orientation": "centre",
            "electorat_cible": ["cadres", "enseignants", "fonctionnaires", "classes_moyennes_supérieures"],
            "budget_base": 6,  # millions d'euros (parti de taille moyenne)
            "adherents_base": 30000,
            "importance": "pivot",
            "sources_financement": ["cotisations", "dons", "financement_public", "evenements", "formations"]
        }
        
    def generate_financial_data(self):
        """Génère des données financières pour le MoDem"""
        print(f"🏛️ Génération des données financières pour {self.parti}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données d'adhérents et structure
        data['Adherents'] = self._simulate_adherents(dates)
        data['Comites_Locaux'] = self._simulate_comites_locaux(dates)
        data['Elus_Locaux'] = self._simulate_elus_locaux(dates)
        data['Elus_Nationaux'] = self._simulate_elus_nationaux(dates)
        data['Elus_Europeens'] = self._simulate_elus_europeens(dates)
        
        # Revenus du parti
        data['Revenus_Total'] = self._simulate_total_revenue(dates)
        data['Cotisations_Adherents'] = self._simulate_membership_fees(dates)
        data['Dons_Prives'] = self._simulate_private_donations(dates)
        data['Financement_Public'] = self._simulate_public_funding(dates)
        data['Revenus_Evenements'] = self._simulate_event_revenue(dates)
        data['Revenus_Formations'] = self._simulate_training_revenue(dates)
        data['Financement_Europeen'] = self._simulate_european_funding(dates)
        
        # Dépenses du parti
        data['Depenses_Total'] = self._simulate_total_expenses(dates)
        data['Depenses_Personnel'] = self._simulate_staff_expenses(dates)
        data['Depenses_Campagnes'] = self._simulate_campaign_expenses(dates)
        data['Depenses_Communication'] = self._simulate_communication_expenses(dates)
        data['Depenses_Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Depenses_Formation'] = self._simulate_training_expenses(dates)
        data['Depenses_Europeennes'] = self._simulate_european_expenses(dates)
        
        # Indicateurs financiers
        data['Taux_Execution_Budget'] = self._simulate_budget_execution_rate(dates)
        data['Ratio_Cotisations_Revenus'] = self._simulate_membership_ratio(dates)
        data['Dependance_Financement_Public'] = self._simulate_public_funding_dependency(dates)
        data['Solde_Financier'] = self._simulate_financial_balance(dates)
        data['Reserves_Financieres'] = self._simulate_financial_reserves(dates)
        
        # Investissements stratégiques
        data['Investissement_Communication'] = self._simulate_communication_investment(dates)
        data['Investissement_Numérique'] = self._simulate_digital_investment(dates)
        data['Investissement_Formation'] = self._simulate_training_investment(dates)
        data['Investissement_Europe'] = self._simulate_european_investment(dates)
        data['Investissement_Prospective'] = self._simulate_prospective_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques au MoDem
        self._add_party_trends(df)
        
        return df
    
    def _simulate_adherents(self, dates):
        """Simule le nombre d'adhérents"""
        base_adherents = self.config["adherents_base"]
        
        adherents = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des adhérents selon les périodes politiques
            if 2007 <= year <= 2008:  # Lancement et élections
                growth_rate = 0.35
            elif 2009 <= year <= 2011:  # Consolidation difficile
                growth_rate = -0.08
            elif 2012 <= year <= 2016:  # Alliance avec le PS
                growth_rate = 0.05
            elif 2017 <= year <= 2022:  # Alliance avec LREM
                growth_rate = 0.15
            else:  # 2023-2025
                growth_rate = 0.03
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.09)
            adherents.append(base_adherents * growth * noise)
        
        return adherents
    
    def _simulate_comites_locaux(self, dates):
        """Simule le nombre de comités locaux"""
        base_comites = 200
        
        comites = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2009:
                growth_rate = 0.20
            elif year <= 2014:
                growth_rate = 0.05
            elif year <= 2020:
                growth_rate = 0.10
            else:
                growth_rate = 0.03
                
            growth = 1 + growth_rate * (i/4)
            comites.append(base_comites * growth)
        
        return comites
    
    def _simulate_elus_locaux(self, dates):
        """Simule le nombre d'élus locaux"""
        base_elus = 2000
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections municipales
            if year in [2008, 2014, 2020]:
                if year == 2008:  # Premières élections
                    multiplier = 1.8
                elif year == 2014:  # Alliance PS
                    multiplier = 1.4
                else:  # 2020 - Alliance LREM
                    multiplier = 1.6
            else:
                multiplier = 1.0
                
            # Tendance générale
            if year <= 2012:
                growth_rate = 0.08
            elif year <= 2017:
                growth_rate = 0.12
            else:
                growth_rate = 0.06
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.07)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_nationaux(self, dates):
        """Simule le nombre d'élus nationaux"""
        base_elus = 10
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections législatives
            if year == 2007:
                multiplier = 3.0  # Premier groupe
            elif year == 2012:
                multiplier = 1.5  # Quelques élus
            elif year == 2017:
                multiplier = 4.5  # Alliance LREM
            elif year == 2022:
                multiplier = 3.8  # Maintien
            else:
                multiplier = 1.0
                
            growth = 1 + 0.08 * (i/2)
            noise = np.random.normal(1, 0.12)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_europeens(self, dates):
        """Simule le nombre d'élus européens"""
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year == 2009:
                elus.append(6)  # Élections européennes 2009
            elif year == 2014:
                elus.append(4)  # Élections européennes 2014
            elif year == 2019:
                elus.append(6)  # Élections européennes 2019
            else:
                # Garder le même nombre entre les élections
                if year > 2019:
                    elus.append(6)
                elif year > 2014:
                    elus.append(4)
                elif year > 2009:
                    elus.append(6)
                else:
                    elus.append(0)
        
        return elus
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Croissance historique des revenus
            if 2007 <= year <= 2008:  # Lancement
                growth_rate = 0.25
            elif 2009 <= year <= 2011:  # Difficultés
                growth_rate = -0.10
            elif 2012 <= year <= 2016:  # Gouvernement avec PS
                growth_rate = 0.08
            elif 2017 <= year <= 2022:  # Gouvernement avec LREM
                growth_rate = 0.20
            else:  # Stabilisation
                growth_rate = 0.05
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_membership_fees(self, dates):
        """Simule les cotisations des adhérents"""
        base_fees = self.config["budget_base"] * 0.25
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2009:
                growth_rate = 0.15
            elif year <= 2014:
                growth_rate = 0.02
            elif year <= 2020:
                growth_rate = 0.10
            else:
                growth_rate = 0.04
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.08)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_private_donations(self, dates):
        """Simule les dons privés"""
        base_donations = self.config["budget_base"] * 0.30
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution selon les alliances
            if year <= 2009:  # Période d'indépendance
                multiplier = 1.1
            elif year <= 2016:  # Alliance PS
                multiplier = 0.9
            elif year <= 2022:  # Alliance LREM
                multiplier = 1.3
            else:
                multiplier = 1.1
                
            # Cycles électoraux
            if year in [2007, 2012, 2017, 2022]:
                electoral_multiplier = 1.7
            else:
                electoral_multiplier = 1.0
                
            growth = 1 + 0.04 * (i/3)
            noise = np.random.normal(1, 0.14)
            donations.append(base_donations * growth * multiplier * electoral_multiplier * noise)
        
        return donations
    
    def _simulate_public_funding(self, dates):
        """Simule le financement public"""
        base_funding = self.config["budget_base"] * 0.25
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Dépend des résultats électoraux
            if year < 2009:
                multiplier = 0.6  # Peu d'élus
            elif year < 2014:
                multiplier = 0.8  # Quelques élus
            elif year < 2017:
                multiplier = 1.2  # Participation gouvernement
            else:
                multiplier = 1.6  # Alliance LREM
                
            growth = 1 + 0.06 * (i/3)
            noise = np.random.normal(1, 0.09)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_event_revenue(self, dates):
        """Simule les revenus des événements"""
        base_revenue = self.config["budget_base"] * 0.08
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Université d'été, conventions, etc.
            if year in [2007, 2012, 2017, 2022]:
                multiplier = 1.8  # Années électorales
            else:
                multiplier = 1.0
                
            growth = 1 + 0.05 * (i/3)
            noise = np.random.normal(1, 0.12)
            revenue.append(base_revenue * growth * multiplier * noise)
        
        return revenue
    
    def _simulate_training_revenue(self, dates):
        """Simule les revenus des formations"""
        base_revenue = self.config["budget_base"] * 0.05
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:  # Développement des formations
                growth = 1 + 0.07 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_european_funding(self, dates):
        """Simule le financement européen"""
        base_funding = self.config["budget_base"] * 0.07
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2009:  # Élus européens
                multiplier = 1.5
            else:
                multiplier = 0.5
                
            growth = 1 + 0.04 * max(0, (year - 2007)/10)
            noise = np.random.normal(1, 0.15)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.92
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2007, 2012, 2017, 2022]:  # Années électorales
                multiplier = 1.5
            else:
                multiplier = 1.0
                
            growth = 1 + 0.05 * (i/3)
            noise = np.random.normal(1, 0.08)
            expenses.append(base_expenses * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_staff_expenses(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.30
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2012:
                growth_rate = 0.10
            elif year <= 2017:
                growth_rate = 0.05
            else:
                growth_rate = 0.08
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.06)
            expenses.append(base_staff * growth * noise)
        
        return expenses
    
    def _simulate_campaign_expenses(self, dates):
        """Simule les dépenses de campagne"""
        base_campaign = self.config["budget_base"] * 0.25
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2007, 2012, 2017, 2022]:  # Années électorales
                multiplier = 2.2
            elif year in [2006, 2011, 2016, 2021]:  # Années pré-électorales
                multiplier = 1.4
            else:
                multiplier = 0.6
                
            growth = 1 + 0.04 * (i/3)
            noise = np.random.normal(1, 0.18)
            expenses.append(base_campaign * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_communication_expenses(self, dates):
        """Simule les dépenses de communication"""
        base_communication = self.config["budget_base"] * 0.15
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2008:
                growth = 1 + 0.08 * max(0, (year - 2008)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.11)
            expenses.append(base_communication * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.12
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            growth = 1 + 0.03 * (i/4)
            noise = np.random.normal(1, 0.05)
            expenses.append(base_operating * growth * noise)
        
        return expenses
    
    def _simulate_training_expenses(self, dates):
        """Simule les dépenses de formation"""
        base_training = self.config["budget_base"] * 0.06
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2009:
                growth = 1 + 0.06 * max(0, (year - 2009)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.09)
            expenses.append(base_training * growth * noise)
        
        return expenses
    
    def _simulate_european_expenses(self, dates):
        """Simule les dépenses européennes"""
        base_european = self.config["budget_base"] * 0.04
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2009:
                growth = 1 + 0.05 * max(0, (year - 2009)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.13)
            expenses.append(base_european * growth * noise)
        
        return expenses
    
    def _simulate_budget_execution_rate(self, dates):
        """Simule le taux d'exécution du budget"""
        rates = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2010:
                base_rate = 0.82
            elif year <= 2016:
                base_rate = 0.85
            else:
                base_rate = 0.88
                
            noise = np.random.normal(1, 0.04)
            rates.append(base_rate * noise)
        
        return rates
    
    def _simulate_membership_ratio(self, dates):
        """Simule le ratio cotisations/revenus"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2010:
                base_ratio = 0.28
            elif year <= 2017:
                base_ratio = 0.25
            else:
                base_ratio = 0.22
                
            noise = np.random.normal(1, 0.05)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_public_funding_dependency(self, dates):
        """Simule la dépendance au financement public"""
        dependencies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2010:
                base_dependency = 0.20
            elif year <= 2017:
                base_dependency = 0.28
            else:
                base_dependency = 0.35
                
            noise = np.random.normal(1, 0.06)
            dependencies.append(base_dependency * noise)
        
        return dependencies
    
    def _simulate_financial_balance(self, dates):
        """Simule le solde financier"""
        balances = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2007, 2012, 2017, 2022]:  # Déficits électoraux
                base_balance = -0.08
            elif year in [2008, 2013, 2018, 2023]:  # Redressement
                base_balance = 0.04
            else:
                base_balance = 0.02
                
            noise = np.random.normal(1, 0.09)
            balances.append(base_balance * noise)
        
        return balances
    
    def _simulate_financial_reserves(self, dates):
        """Simule les réserves financières"""
        base_reserves = self.config["budget_base"] * 0.4
        
        reserves = []
        current_reserves = base_reserves
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2007, 2012, 2017, 2022]:  # Utilisation des réserves
                change_rate = -0.15
            elif year in [2008, 2013, 2018, 2023]:  # Reconstitution
                change_rate = 0.10
            else:
                change_rate = 0.03
                
            current_reserves *= (1 + change_rate)
            noise = np.random.normal(1, 0.08)
            reserves.append(current_reserves * noise)
        
        return reserves
    
    def _simulate_communication_investment(self, dates):
        """Simule l'investissement en communication"""
        base_investment = self.config["budget_base"] * 0.09
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2008:
                growth = 1 + 0.10 * max(0, (year - 2008)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_digital_investment(self, dates):
        """Simule l'investissement numérique"""
        base_investment = self.config["budget_base"] * 0.07
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2012:
                growth = 1 + 0.15 * max(0, (year - 2012)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.17)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement en formation"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2009:
                growth = 1 + 0.08 * max(0, (year - 2009)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_european_investment(self, dates):
        """Simule l'investissement européen"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2009:
                growth = 1 + 0.06 * max(0, (year - 2009)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_prospective_investment(self, dates):
        """Simule l'investissement en prospective"""
        base_investment = self.config["budget_base"] * 0.03
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:
                growth = 1 + 0.05 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _add_party_trends(self, df):
        """Ajoute des tendances réalistes pour le MoDem"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Création du MoDem (2007)
            if year == 2007:
                df.loc[i, 'Revenus_Total'] *= 1.6
                df.loc[i, 'Adherents'] *= 2.2
            
            # Élection présidentielle 2007 (score de Bayrou)
            if year == 2007:
                df.loc[i, 'Dons_Prives'] *= 2.5
                df.loc[i, 'Depenses_Campagnes'] *= 2.8
            
            # Européennes 2009
            if year == 2009:
                df.loc[i, 'Elus_Europeens'] = 6
                df.loc[i, 'Financement_Europeen'] *= 1.8
            
            # Alliance avec le PS (2012)
            if year == 2012:
                df.loc[i, 'Financement_Public'] *= 1.4
                df.loc[i, 'Elus_Nationaux'] *= 1.6
            
            # Participation au gouvernement (2012-2016)
            if 2012 <= year <= 2016:
                df.loc[i, 'Revenus_Total'] *= 1.15
                df.loc[i, 'Depenses_Personnel'] *= 1.10
            
            # Alliance avec LREM (2017)
            if year == 2017:
                df.loc[i, 'Revenus_Total'] *= 1.4
                df.loc[i, 'Financement_Public'] *= 1.6
                df.loc[i, 'Elus_Nationaux'] *= 4.5
                df.loc[i, 'Adherents'] *= 1.2
            
            # Européennes 2019
            if year == 2019:
                df.loc[i, 'Elus_Europeens'] = 6
                df.loc[i, 'Investissement_Europe'] *= 1.5
            
            # Réélection 2022
            if year == 2022:
                df.loc[i, 'Depenses_Campagnes'] *= 1.8
                df.loc[i, 'Dons_Prives'] *= 1.4
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances du MoDem"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Adhérents et structure
        ax4 = plt.subplot(4, 2, 4)
        self._plot_membership_structure(df, ax4)
        
        # 5. Investissements stratégiques
        ax5 = plt.subplot(4, 2, 5)
        self._plot_strategic_investments(df, ax5)
        
        # 6. Indicateurs financiers
        ax6 = plt.subplot(4, 2, 6)
        self._plot_financial_indicators(df, ax6)
        
        # 7. Évolution des élus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_elected_officials(df, ax7)
        
        # 8. Situation financière
        ax8 = plt.subplot(4, 2, 8)
        self._plot_financial_situation(df, ax8)
        
        plt.suptitle(f'Analyse des Finances du {self.parti} ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'Modem_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Total'], label='Revenus Totaux', 
               linewidth=2, color='#FF9900', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Total'], label='Dépenses Totales', 
               linewidth=2, color='#FF6600', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les événements clés
        key_events = {2007: 'Création MoDem', 2009: 'Européennes', 
                     2012: 'Alliance PS', 2017: 'Alliance LREM', 2022: 'Législatives'}
        
        for year, event in key_events.items():
            if year in df['Annee'].values:
                y_val = df[df['Annee'] == year]['Revenus_Total'].values[0]
                ax.annotate(event, (year, y_val), xytext=(10, 10), 
                           textcoords='offset points', fontsize=8, 
                           arrowprops=dict(arrowstyle='->', alpha=0.6))
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Cotisations_Adherents', 'Dons_Prives', 'Financement_Public', 
                     'Revenus_Evenements', 'Revenus_Formations', 'Financement_Europeen']
        colors = ['#FF9900', '#FFCC00', '#FF6600', '#CC9900', '#FF9933', '#CC6600']
        labels = ['Cotisations', 'Dons Privés', 'Financement Public', 
                 'Événements', 'Formations', 'Financement Européen']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Depenses_Personnel', 'Depenses_Campagnes', 'Depenses_Communication',
                     'Depenses_Fonctionnement', 'Depenses_Formation', 'Depenses_Europeennes']
        colors = ['#FF9900', '#FFCC00', '#FF6600', '#CC9900', '#FF9933', '#CC6600']
        labels = ['Personnel', 'Campagnes', 'Communication', 'Fonctionnement', 'Formation', 'Dépenses Européennes']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_membership_structure(self, df, ax):
        """Plot des adhérents et structure"""
        # Adhérents
        ax.bar(df['Annee'], df['Adherents']/1000, label='Adhérents (milliers)', 
              color='#FF9900', alpha=0.7)
        
        ax.set_title('Adhérents et Structure Locale', fontsize=12, fontweight='bold')
        ax.set_ylabel('Adhérents (milliers)', color='#FF9900')
        ax.tick_params(axis='y', labelcolor='#FF9900')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Comités locaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Comites_Locaux'], label='Comités Locaux', 
                linewidth=2, color='#FF6600')
        ax2.set_ylabel('Comités Locaux', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_strategic_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_Communication'], label='Communication', 
               linewidth=2, color='#FF9900', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Numérique'], label='Numérique', 
               linewidth=2, color='#FF6600', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
               linewidth=2, color='#FFCC00', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Europe'], label='Europe', 
               linewidth=2, color='#CC9900', alpha=0.8)
        
        ax.set_title('Investissements Stratégiques (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_financial_indicators(self, df, ax):
        """Plot des indicateurs financiers"""
        # Taux d'exécution budgétaire
        ax.bar(df['Annee'], df['Taux_Execution_Budget']*100, label='Taux d\'Exécution (%)', 
              color='#FF9900', alpha=0.7)
        
        ax.set_title('Indicateurs Financiers', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux d\'Exécution (%)', color='#FF9900')
        ax.tick_params(axis='y', labelcolor='#FF9900')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Dépendance financement public en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Dependance_Financement_Public']*100, label='Dépendance Financement Public (%)', 
                linewidth=3, color='#FF6600')
        ax2.set_ylabel('Dépendance Financement Public (%)', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_elected_officials(self, df, ax):
        """Plot de l'évolution des élus"""
        ax.plot(df['Annee'], df['Elus_Locaux'], label='Élus Locaux', 
               linewidth=2, color='#FF9900', alpha=0.8)
        
        ax.set_title('Évolution des Élus', fontsize=12, fontweight='bold')
        ax.set_ylabel('Élus Locaux', color='#FF9900')
        ax.tick_params(axis='y', labelcolor='#FF9900')
        ax.grid(True, alpha=0.3)
        
        # Élus nationaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Elus_Nationaux'], label='Élus Nationaux', 
                linewidth=2, color='#FF6600', alpha=0.8)
        ax2.set_ylabel('Élus Nationaux', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_financial_situation(self, df, ax):
        """Plot de la situation financière"""
        # Solde financier
        ax.bar(df['Annee'], df['Solde_Financier']*100, label='Solde Financier (% du budget)', 
              color=df['Solde_Financier'].apply(lambda x: '#009900' if x > 0 else '#FF6600'), alpha=0.7)
        
        ax.set_title('Situation Financière', fontsize=12, fontweight='bold')
        ax.set_ylabel('Solde Financier (% du budget)', color='#FF9900')
        ax.tick_params(axis='y', labelcolor='#FF9900')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Réserves financières en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Reserves_Financieres'], label='Réserves Financières (M€)', 
                linewidth=3, color='#FF6600')
        ax2.set_ylabel('Réserves Financières (M€)', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques pour le MoDem"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - {self.parti} ({self.start_year}-{self.end_year})")
        print("=" * 70)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Revenus_Total'].mean()
        avg_expenses = df['Depenses_Total'].mean()
        avg_adherents = df['Adherents'].mean()
        avg_execution = df['Taux_Execution_Budget'].mean() * 100
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Adhérents moyens: {avg_adherents:,.0f} personnes")
        print(f"Taux d'exécution budgétaire moyen: {avg_execution:.1f}%")
        
        # 2. Croissance historique
        print("\n2. 📊 ÉVOLUTION HISTORIQUE:")
        revenue_growth = ((df['Revenus_Total'].iloc[-1] / 
                          df['Revenus_Total'].iloc[0]) - 1) * 100
        adherents_growth = ((df['Adherents'].iloc[-1] / 
                           df['Adherents'].iloc[0]) - 1) * 100
        
        print(f"Évolution des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Évolution des adhérents ({self.start_year}-{self.end_year}): {adherents_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        membership_share = (df['Cotisations_Adherents'].mean() / df['Revenus_Total'].mean()) * 100
        donations_share = (df['Dons_Prives'].mean() / df['Revenus_Total'].mean()) * 100
        public_funding_share = (df['Financement_Public'].mean() / df['Revenus_Total'].mean()) * 100
        european_funding_share = (df['Financement_Europeen'].mean() / df['Revenus_Total'].mean()) * 100
        
        print(f"Part des cotisations dans les revenus: {membership_share:.1f}%")
        print(f"Part des dons privés: {donations_share:.1f}%")
        print(f"Part du financement public: {public_funding_share:.1f}%")
        print(f"Part du financement européen: {european_funding_share:.1f}%")
        
        # 4. Performance et efficacité
        print("\n4. 🎯 PERFORMANCE FINANCIÈRE:")
        avg_balance = df['Solde_Financier'].mean() * 100
        last_reserves = df['Reserves_Financieres'].iloc[-1]
        dependency_public = df['Dependance_Financement_Public'].iloc[-1] * 100
        
        print(f"Solde financier moyen: {avg_balance:.1f}% du budget")
        print(f"Réserves financières finales: {last_reserves:.1f} M€")
        print(f"Dépendance au financement public: {dependency_public:.1f}%")
        
        # 5. Spécificités du MoDem
        print(f"\n5. 🌟 SPÉCIFICITÉS DU MOUVEMENT DÉMOCRATE:")
        print(f"Orientation politique: {self.config['orientation']}")
        print(f"Électorat cible: {', '.join(self.config['electorat_cible'])}")
        print(f"Sources de financement: {', '.join(self.config['sources_financement'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2007: Création du MoDem par François Bayrou")
        print("• 2007: Score important à l'élection présidentielle")
        print("• 2009: Bon score aux élections européennes")
        print("• 2012: Alliance avec le Parti Socialiste")
        print("• 2012-2016: Participation au gouvernement")
        print("• 2017: Alliance avec La République En Marche")
        print("• 2017-2022: Participation au gouvernement")
        print("• 2019: Élections européennes")
        print("• 2022: Réélection des députés MoDem")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Maintenir la position pivot au centre")
        print("• Renforcer l'autonomie financière")
        print("• Développer le fundraising auprès des entreprises")
        print("• Optimiser l'utilisation du financement européen")
        print("• Investir dans la formation des cadres centristes")
        print("• Renforcer l'ancrage local et territorial")
        print("• Développer les think tanks et la prospective")
        print("• Préparer les futures alliances électorales")

def main():
    """Fonction principale pour l'analyse du MoDem"""
    print("🏛️ ANALYSE DES FINANCES DU MOUVEMENT DÉMOCRATE (2007-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = ModemFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'Modem_financial_data_2007_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Adherents', 'Revenus_Total', 'Depenses_Total', 'Taux_Execution_Budget']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des finances du {analyzer.parti} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Revenus, dépenses, adhérents, élus, indicateurs financiers")

if __name__ == "__main__":
    main()