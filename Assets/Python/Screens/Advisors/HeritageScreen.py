
from CvPythonExtensions import *
import CvScreensInterface as UP
import HandleInputUtil

# globals
GC = CyGlobalContext()
AFM = CyArtFileMgr()
GTM = CyGameTextMgr()
TRNSLTR = CyTranslator()
GAME = GC.getGame()

class HeritageScreen:

	def __init__(self, screenId):
		self.screenId = screenId

	def getScreen(self):
		return CyGInterfaceScreen("HeritageScreen", self.screenId)

	def interfaceScreen(self):

		screen = self.getScreen()
		if screen.isActive():
			return

		import DebugUtils
		self.bDebug = DebugUtils.isAnyDebugMode()

		import InputData
		self.InputData = InputData.instance

		import PythonToolTip
		self.tooltip = PythonToolTip.PythonToolTip()

		# Resolution
		import ScreenResolution as SR
		self.xRes = xRes = SR.x
		self.yRes = yRes = SR.y
		self.xMid = xMid = xRes / 2

		if yRes > 1000:
			self.H_EDGE = H_EDGE = 38
			uFontEdge = "<font=4b>"
		elif yRes > 800:
			self.H_EDGE = H_EDGE = 32
			uFontEdge = "<font=3b>"
		else:
			self.H_EDGE = H_EDGE = 29
			uFontEdge = "<font=2b>"

		if xRes > 1700:
			self.iSize = 64
			self.aFontList = aFontList = [uFontEdge, "<font=4b>", "<font=4>", "<font=3b>", "<font=3>", "<font=2b>", "<font=2>"]
			self.iOff = 8
		elif xRes > 1400:
			self.iSize = 56
			self.aFontList = aFontList = [uFontEdge, "<font=3b>", "<font=3>", "<font=2b>", "<font=2>", "<font=1b>", "<font=1>"]
			self.iOff = 6
		else:
			self.iSize = 48
			self.aFontList = aFontList = [uFontEdge, "<font=2b>", "<font=2>", "<font=1b>", "<font=1>", "<font=0b>", "<font=0>"]
			self.iOff = 4

		Y_BOT_TEXT = yRes - H_EDGE + 8

		H_STAT_BAR = 7*H_EDGE/3
		self.Y_STAT_BAR = Y_STAT_BAR = yRes - H_STAT_BAR
		self.Y_MID_STAT_BAR = y = Y_STAT_BAR + (H_STAT_BAR - H_EDGE)/2 - 6

		# Caching
		self.iTab = 0
		self.iPlayer = iPlayer = GAME.getActivePlayer()
		self.CyPlayer = GC.getPlayer(iPlayer)
		self.team = GC.getTeam(self.CyPlayer.getTeam())
		self.HILITE = AFM.getInterfaceArtInfo("BUTTON_HILITE_SQUARE").getPath()
		self.CANCEL = AFM.getInterfaceArtInfo("INTERFACE_BUTTONS_CANCEL").getPath()
		self.aWidgetBucket = []
		self.nWidgetCount = 0
		self.xTraits = x0 = xRes/2 + 8
		self.yTraits = y0 = H_EDGE + 32
		self.hTraits = h0 = yRes - y0 - H_EDGE

		# Base Screen
		eWidGen = WidgetTypes.WIDGET_GENERAL
		eFontTitle = FontTypes.TITLE_FONT

		screen.setRenderInterfaceOnly(True)
		screen.showWindowBackground(False)
		screen.setDimensions(0, 0, xRes, yRes)

		screen.addDDSGFC("Heritage_BG", AFM.getInterfaceArtInfo("SCREEN_BG_OPAQUE").getPath(), 0, 0, xRes, yRes, eWidGen, 1, 1)
		screen.addPanel("TopPanel", "", "", True, False, 0, 0, xRes, H_EDGE, PanelStyles.PANEL_STYLE_TOPBAR)
		screen.addPanel("BottomPanel", "", "", True, False, 0, yRes - H_EDGE, xRes, H_EDGE, PanelStyles.PANEL_STYLE_BOTTOMBAR)


		screen.setLabel("Header", "", uFontEdge + TRNSLTR.getText("TXT_KEY_HUD_BUTTON_ADVISOR_HERITAGE",()), 1<<2, xRes / 2, 2, 0, eFontTitle, eWidGen, 0, 0)
		szTxt = uFontEdge + TRNSLTR.getText("TXT_WORD_EXIT", ())
		screen.setText("HeritageExit", "", szTxt, 1<<1, xRes - 8, 0, 0, eFontTitle, WidgetTypes.WIDGET_CLOSE_SCREEN, -1, -1)

		# Tabs
		szCol = "<color=255,255,0>"
		szTxt = uFontEdge + "Heritage"
		dX = xMid
		x = dX / 2
		screen.setText("Heritage_Tab0", "", szTxt, 1<<2, x, Y_BOT_TEXT, 0, eFontTitle, eWidGen, 0, 0)
		screen.setText("Heritage_Tab|Col0", "", szCol + szTxt, 1<<2, x, Y_BOT_TEXT, 0, eFontTitle, eWidGen, 0, 0)
		screen.hide("Heritage_Tab0")

		szTxt = uFontEdge + "Traits"
		x += dX
		screen.setText("Heritage_Tab1", "", szTxt, 1<<2, x, Y_BOT_TEXT, 0, eFontTitle, eWidGen, 0, 0)
		screen.setText("Heritage_Tab|Col1", "", szCol + szTxt, 1<<2, x, Y_BOT_TEXT, 0, eFontTitle, eWidGen, 0, 0)
		screen.hide("Heritage_Tab|Col1")

		# Debug
		if self.bDebug:
			DD = "Heritage_DebugDD"
			screen.addDropDownBoxGFC(DD, H_EDGE, 0, 300, eWidGen, 1, 1, FontTypes.GAME_FONT)
			for iPlayerX in xrange(GC.getMAX_PLAYERS()):
				CyPlayerX = GC.getPlayer(iPlayerX)
				if CyPlayerX.isAlive():
					screen.addPullDownString(DD, CyPlayerX.getName(), iPlayerX, iPlayerX, iPlayerX == iPlayer)

		# Draw Contents
		self.drawContents(screen)
		screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)


	# Draw the contents...
	def drawContents(self, screen):
		self.deleteAllWidgets(screen)
		if not self.iTab:
			self.drawHeritage(screen)
		elif self.iTab == 1:
			self.drawTraits(screen)

	def drawHeritage(self, screen):
		H_EDGE = self.H_EDGE
		CANCEL = self.CANCEL
		player = self.CyPlayer

		uFontEdge, uFont4b, uFont4, uFont3b, uFont3, uFont2b, uFont2 = self.aFontList

		eWidGen = WidgetTypes.WIDGET_GENERAL
		eFontGame = FontTypes.GAME_FONT
		iPanelBlue50 = PanelStyles.PANEL_STYLE_BLUE50

		# Background
		h0 = self.yRes - 2*H_EDGE
		w0 = (self.xRes - 52)/4
		w1 = 2*w0+12
		x0 = 8
		x1 = 20 + w0
		x2 = 32 + w0*2
		screen.addPanel(self.getNextWidget(), "", "", True, False, x0, H_EDGE, w0, h0, iPanelBlue50)
		screen.addPanel(self.getNextWidget(), "", "", True, False, x1, H_EDGE, w0, h0, iPanelBlue50)
		screen.addPanel(self.getNextWidget(), "", "", True, False, x2, H_EDGE, w1, h0, iPanelBlue50)
		# Main Area
		ScPnl0 = self.getNextWidget()
		screen.addScrollPanel(ScPnl0, "", x0-8, H_EDGE+8, w0+12, h0-42, PanelStyles.PANEL_STYLE_EMPTY)
		screen.setStyle(ScPnl0, "ScrollPanel_Alt_Style")
		ScPnl1 = self.getNextWidget()
		screen.addScrollPanel(ScPnl1, "", x1-8, H_EDGE+8, w0+12, h0-42, PanelStyles.PANEL_STYLE_EMPTY)
		screen.setStyle(ScPnl1, "ScrollPanel_Alt_Style")
		# Fill screen
		iSize = self.iSize * 2/3
		dy = iSize + 8
		y0 = y1 = 0
		iOff = self.iOff
		for iType in xrange(GC.getNumHeritageInfos()):
			heritageX = GC.getHeritageInfo(iType)

			if player.hasHeritage(iType):
				screen.setImageButtonAt("WID|HERITAGE|IMG%d" % iType, ScPnl1, heritageX.getButton(), 8, y1, iSize, iSize, eWidGen, 1, 2)
				screen.setTextAt("WID|HERITAGE|TEXT%d" % iType, ScPnl1, uFont3b + heritageX.getDescription(), 1<<0, 2+dy, iOff + y1, 0, eFontGame, eWidGen, 1, 2)
				y1 += dy
			else:
				screen.addDDSGFCAt("", ScPnl0, heritageX.getButton(), 8, y0, iSize, iSize, eWidGen, 1, 1, False)
				screen.setImageButtonAt("WID|HERITAGE|IMG%d" % iType, ScPnl0, CANCEL, 8, y0, iSize, iSize, eWidGen, 1, 2)
				screen.setTextAt("WID|HERITAGE|TEXT%d" % iType, ScPnl0, uFont3 + heritageX.getDescription(), 1<<0, 2+dy, iOff + y0, 0, eFontGame, eWidGen, 1, 2)
				y0 += dy


	def drawTraits(self, screen):
		xRes = self.xRes
		yRes = self.yRes
		xMid = self.xMid
		H_EDGE = self.H_EDGE
		iPlayer = self.iPlayer
		team = self.team

		uFontEdge, uFont4b, uFont4, uFont3b, uFont3, uFont2b, uFont2 = self.aFontList

		x0 = self.xTraits
		y0 = self.yTraits
		h0 = self.hTraits
		w0 = xRes/2 - 16

		DD = "TraitsDD_Players"
		self.aWidgetBucket.append(DD)
		screen.addDropDownBoxGFC(DD, x0, H_EDGE, w0, WidgetTypes.WIDGET_GENERAL, 1, 2, FontTypes.GAME_FONT)
		if self.bDebug:
			range = GC.getMAX_PLAYERS()
		else: range = GC.getMAX_PC_PLAYERS()

		for iPlayerX in xrange(range):
			playerX = GC.getPlayer(iPlayerX)
			if playerX.isAlive() and (iPlayerX == iPlayer or team.isHasMet(playerX.getTeam())):
				screen.addPullDownString(DD, playerX.getName(), iPlayerX, iPlayerX, iPlayerX == iPlayer)

		pnl = self.getNextWidget()
		screen.addPanel(pnl, "", "", False, False, x0, y0, w0, h0, PanelStyles.PANEL_STYLE_BLUE50)

		self.aWidgetBucket.append("TraitsMultiLine")
		self.fillTraitsPanel(screen, iPlayer)


	def fillTraitsPanel(self, screen, iPlayer):
		player = GC.getPlayer(iPlayer)
		txt = ""
		for iTrait in xrange(GC.getNumTraitInfos()):
			if player.hasTrait(iTrait):
				if txt:
					txt += "\n\n"
				txt += GTM.parseTraits(iTrait, False, False)

		screen.addMultilineText(
			"TraitsMultiLine",
			self.aFontList[4] + txt,
			self.xTraits + 8, self.yTraits + 14,
			self.xRes/2 - 26, self.hTraits - 26,
			WidgetTypes.WIDGET_GENERAL, 1, 2, 1<<0
		)


	# Utility
	def getNextWidget(self):
		szName = "Heritage_Widget" + str(self.nWidgetCount)
		self.nWidgetCount += 1
		return szName

	def deleteAllWidgets(self, screen):
		# Generic widgets
		iNumWidgets = self.nWidgetCount
		self.nWidgetCount = 0
		for i in xrange(iNumWidgets):
			screen.deleteWidget(self.getNextWidget())
		self.nWidgetCount = 0
		# Specific widgets
		for widget in self.aWidgetBucket:
			screen.deleteWidget(widget)
		self.aWidgetBucket = []

	#--------------------------#
	# Base operation functions #
	#||||||||||||||||||||||||||#
	def update(self, fDelta):
		if self.tooltip.bLockedTT:
			self.tooltip.handle(self.getScreen())

	def handleInput(self, inputClass):
		screen = self.getScreen()
		if not screen.isActive():
			return
		HandleInputUtil.debugInput(inputClass)
		bAlt, bCtrl, bShift = self.InputData.getModifierKeys()
		iCode	= inputClass.eNotifyCode
		iData	= inputClass.iData
		ID		= inputClass.iItemID
		NAME	= inputClass.szFunctionName
		iBtn	= inputClass.iButtonType
		iData1	= inputClass.iData1
		iData2	= inputClass.iData2
		szFlag	= HandleInputUtil.MOUSE_FLAGS.get(inputClass.uiFlags, "UNKNOWN")

		szSplit = NAME.split("|")
		BASE = szSplit[0]
		if szSplit[1:]:
			TYPE = szSplit[1]
		else:
			TYPE = ""
		if szSplit[2:]:
			CASE = szSplit[2:]
		else:
			CASE = [0]

		self.tooltip.reset(screen)

		if iCode == NotifyCode.NOTIFY_CURSOR_MOVE_ON:

			if BASE == "WID":

				if TYPE == "HERITAGE":
					self.tooltip.handle(screen, GTM.getHeritageHelp(ID, None, True, False, False), uFont=self.aFontList[4])

		elif iCode == NotifyCode.NOTIFY_CLICKED:

			if BASE == "Heritage_Tab":
				if CASE[0] != "Col":
					screen.hide("Heritage_Tab|Col" + str(self.iTab))
					screen.show("Heritage_Tab" + str(self.iTab))
					screen.hide("Heritage_Tab" + str(ID))
					screen.show("Heritage_Tab|Col" + str(ID))
					self.iTab = ID
					self.drawContents(screen)

			elif BASE == "WID":

				if TYPE == "HERITAGE":
					UP.pediaJumpToHeritage([ID])


		elif iCode == NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED:
			if NAME == "Heritage_DebugDD":
				self.iPlayer = screen.getPullDownData(NAME, screen.getSelectedPullDownID(NAME))
				self.CyPlayer = GC.getPlayer(self.iPlayer)
				self.drawContents(screen)

			elif NAME == "TraitsDD_Players":
				self.fillTraitsPanel(screen, screen.getPullDownData(NAME, screen.getSelectedPullDownID(NAME)))


	def onClose(self):
		# Clean up
		screen = self.getScreen()
		screen.setDying(True)
		del self.InputData, self.nWidgetCount, self.CyPlayer, self.iPlayer, \
			self.xRes, self.yRes, self.xMid, self.iSize, self.aFontList, self.aWidgetBucket, \
			self.H_EDGE, self.Y_STAT_BAR, self.Y_MID_STAT_BAR, self.iOff, \
			self.bDebug, self.HILITE, self.CANCEL, self.iTab, \
			self.xTraits, self.yTraits, self.hTraits
