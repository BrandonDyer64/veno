import string

##
## @brief      Class for keyboard.
##
class Keyboard:
	##
	## @brief      Constructs the object.
	##
	## @param      self     The object
	## @param      manager  The manager to allow scheduling actions in external Windows
	##
	def __init__(self, manager):
		self.manager = manager
		self.bindings = self.createBindings()

	##
	## @brief      Update. grab key and do something with it.
	##
	## @param      self  The object
	##
	def update(self):
		while True:
			c = self.manager.stdscr.getch()
			self.manager.stdscr.timeout(30)
			if c == -1:
				self.manager.stdscr.timeout(-1)
				break
			c = self.manager.curses.keyname(c).decode("utf-8")
			if c == "^I":
				self.bindings[c]("\t")
				continue
			if c in self.bindings:
				self.bindings[c]()
				continue
			if c in string.printable:
				self.bindings["printable-character"](c)
				continue

	##
	## @brief      Terminate Keyboard Manager
	##
	## @param      self  The object
	##
	def terminate(self):
		pass

	##
	## @brief      Binds all keybindings to binding dictionary. Saved as "keyname"->function instance
	##
	## @param      self  The object
	##
	def createBindings(self):
		fileWindow = self.manager.Windows["fileWindow"]
		magicBar = self.manager.Windows["magicBar"]
		colorCustomizer = self.manager.Windows["colorCustomizer"]
		return {
			"KEY_UP": fileWindow.moveFilecursorUp,
			"KEY_DOWN": fileWindow.moveFilecursorDown,
			"KEY_LEFT": fileWindow.moveFilecursorLeft,
			"KEY_RIGHT": fileWindow.moveFilecursorRight,
			"printable-character": fileWindow.enterTextAtFilecursor,
			"KEY_BACKSPACE": fileWindow.backspaceTextAtFilecursor,
			"KEY_DC": fileWindow.deleteTextAtFilecursor,
			"KEY_END": fileWindow.gotoEndOfLine,
			"KEY_F(3)": fileWindow.gotoStartOfFile,
			"KEY_F(4)": fileWindow.gotoEndOfFile,
			"KEY_HOME": fileWindow.gotoStartOfLine,
			"KEY_NPAGE": fileWindow.scrollDown,
			"KEY_PPAGE": fileWindow.scrollUp,
			"^D": fileWindow.deleteLineAtFilecursor,
			"^J": fileWindow.newLineAtFilecursor,
			"^W": fileWindow.saveFile,
			"^I": fileWindow.enterTextAtFilecursor,
			"^F": magicBar.search,
			"^L": magicBar.gotoLine,
			"^G": magicBar.searchNext,
			"^H": magicBar.replace,
			"^_": colorCustomizer.toggle,
			"^B": fileWindow.toggleSelect,
			"^?": fileWindow.backspaceTextAtFilecursor,
			"^K": fileWindow.copySelect,
			"^V": fileWindow.pasteAtFilecursor,
			"^X": fileWindow.cutSelect,
			"kRIT5": fileWindow.moveViewportRight,
			"kLFT5": fileWindow.moveViewportLeft,
			"kUP5": fileWindow.moveViewportUp,
			"kDN5": fileWindow.moveViewportDown
		}
