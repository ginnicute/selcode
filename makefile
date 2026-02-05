.PHONY: install uninstall

install:
	@echo "Installing selcode..."
	@chmod +x selcode.py
	@sudo cp selcode.py /usr/local/bin/selcode
	@echo "Installation complete! Try 'selcode --help'"

uninstall:
	@echo "Uninstalling selcode..."
	@sudo rm -f /usr/local/bin/selcode
	@echo "Uninstallation complete"
