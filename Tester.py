'''
	This program was written by Roy W. Gero.
	If you have questions, comments or concerns please contact him on GitHub
'''

from Penalty import *
from scanning_games import *
from gameDayProcessor import *
import unittest,os,sys

class TestingPenaltyClass(unittest.TestCase):
	def testPlayerName(self):
		self.assertEqual(event.getPlayer(), "Roy Gero")
		
	def testPlayerTeam(self):
		self.assertEqual(event.getTeam(), "Colorado Avalanche")
		
	def testPenalty(self):
		self.assertEqual(event.getPenalty(), "Too Much Man")
	
	def testSide(self):
		self.assertEqual(event.getSide(), "Home")
		
	def testOpponent(self):
		self.assertEqual(event.getOpponent(), "Calgary Flames")
		
	def testDate(self):
		self.assertEqual(event.getDate(), "July 8, 2015")
	
	def testRef(self):
		self.assertEqual(event.getRefs(), ["Don","Ron"])
		
	def testPrint(self):
		self.assertEqual(event.printEvent(),"Roy Gero | Colorado Avalanche | Too Much Man | July 8, 2015 | Calgary Flames | Home | Don, Ron")
		
	def testTablePrint(self):
		self.assertEqual(event.printTable(),"<tr><td>Roy Gero<//td><td>Colorado Avalanche<//td><td>Too Much Man<//td><td>July 8, 2015<//td><td>Calgary Flames<//td><td>Home<//td><td>Don, Ron<//td><//tr>")
	

		
class TestingSGMethods(unittest.TestCase):
	def testTeamsPlaying(self):
		self.assertEqual(teamsPlaying(scan),["Montreal Canadiens", "Toronto Maple Leafs"])
	
	def testRefsInGame(self):
		self.assertEqual(refsInGame(scan),["Paul Devorski", "Tom Kowal"])
	
	def testDate(self):
		self.assertEqual(getDateFromFile(scan),"10/08/2014")
		
	def testProcessFile(self):
		self.assertEqual(len(processData(scan)),4)
		
	def testingProcessingFromFile(self):
		procedurallyGenerated = processData(scan)
		testingFile = open("TestingDocs\ProcessingFromFileTest.txt","r")
		readingFromFile = processFromFile(testingFile)
		self.assertEqual(len(procedurallyGenerated), len(readingFromFile))
		for i in range(0,len(procedurallyGenerated)):
			pG = procedurallyGenerated[i]
			fF = readingFromFile[i]
			self.assertTrue(pG.getPlayer()==fF.getPlayer(), pG.getPlayer() + " : " + fF.getPlayer() + " in entry " + str(i))
			self.assertTrue(pG.getTeam()==fF.getTeam(), pG.getTeam() + " : " + fF.getTeam() + " in entry " + str(i))
			self.assertTrue(pG.getPenalty()==fF.getPenalty(), pG.getPenalty() + " : " + fF.getPenalty() + " in entry " + str(i))
			self.assertTrue(pG.getSide()==fF.getSide(), pG.getSide() + " : " + 
				fF.getSide() + " in entry " + str(i))
			self.assertTrue(pG.getOpponent()==fF.getOpponent(), pG.getOpponent() + " : " + 
				fF.getOpponent() + " in entry " + str(i))
			self.assertTrue(pG.getDate()==fF.getDate(), pG.getDate() + " : " + 
				fF.getDate() + " in entry " + str(i))
			self.assertTrue(pG.getRefsAsString()==fF.getRefsAsString(), pG.getRefsAsString() + " : " + fF.getRefsAsString() + " in entry " + str(i))
	

class TestingGDPMethods(unittest.TestCase):
	def testFirstDate(self):
		self.assertEqual(formatDate("2015-09-04"),"09/04/2015")
	
	def testProcessGameDay(self):
		dateProcessing("02/26/2015", ".\\TestingDocs\\TestingGDP_Data.txt")
		try:
			newFile = open(".\\TestingDocs\\TestingGDP_Data.txt", 'r')
			oldFile = open(".\\TestingDocs\\02-26-2015.txt",'r')
		except:
			self.assertTrue(False) #If either file doesn't exist, bail out.
		newData = newFile.read()
		oldData = oldFile.read()
		newFile.close()
		oldFile.close()
		self.assertEqual(newData,oldData)	#Compares the data
		
		#Removes the created test file
		os.remove(".\\TestingDocs\\TestingGDP_Data.txt")
		
	def testProcessingGameDay2(self):
		dateProcessing("10/17/2014", ".\\TestingDocs\\TestingGDP_Data.txt")
		try:
			newFile = open(".\\TestingDocs\\TestingGDP_Data.txt", 'r')
			oldFile = open(".\\TestingDocs\\10-17-2014.txt",'r')
		except:
			self.assertTrue(False) #If either file doesn't exist, bail out.
		newData = newFile.read()
		oldData = oldFile.read()
		newFile.close()
		oldFile.close()
		self.assertEqual(newData,oldData)	#Compares the data
		
		#Removes the created test file
		os.remove(".\\TestingDocs\\TestingGDP_Data.txt")
		
		
	
	
'''
// Setting up Data
'''	
os.system("cls")		
event = Penalty("Roy Gero","Colorado Avalanche","Too Much Man",True,"Calgary Flames","July 8, 2015",["Don","Ron"])

#Setting up a dummy file
file_name = "TestingDocs\\Testing.htm"
file = open(file_name,'r')
scan = file.read()

	  
print "Testing the class constructor and get functions. (8 Tests)"
print "--------------------------------------------------------"
penaltyClassSuite = unittest.TestLoader().loadTestsFromTestCase(TestingPenaltyClass)
unittest.TextTestRunner(verbosity=2).run(penaltyClassSuite)

print "\nTesting the functions in scanning_games using \"" + file_name + "\""
print "--------------------------------------------------------"
sgFileSuite = unittest.TestLoader().loadTestsFromTestCase(TestingSGMethods)
unittest.TextTestRunner(verbosity=2).run(sgFileSuite)

print "Testing the methods in gameDayProcessor. (1 Test)"
print "--------------------------------------------------------"
gdpFileSuite = unittest.TestLoader().loadTestsFromTestCase(TestingGDPMethods)
unittest.TextTestRunner(verbosity=2).run(gdpFileSuite)
