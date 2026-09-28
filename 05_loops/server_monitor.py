while True:
    print("================================")
    print("     SERVER MONITORING SYSTEM")
    print("================================")
    print("1. Check Servers")
    print("2. Show Security Scan")
    print("3. Show System Modules")
    print("4. Shutdown")

    choice = input("Enter your choice: ")

    if choice == "1":
        for x in range(1, 11):
            if x % 3 == 0:
                print("Server", x, ": WARNING")
            else:
                print("Server", x, ": ONLINE")

    elif choice == "2":
        checks = int(input("Enter number of security checks: "))
        check = 1

        while check <= checks:
            print("Security Check", check, ": PASS")

            if check >= 7:
                print("Critical security check detected!")
                print("Scan stopped.")
                break

            check = check + 1

    elif choice == "3":
        for group in range(1, 4):
            print("Module Group", group)

            for module in range(1, 4):
                print("  Module", module)

    elif choice == "4":
        print("System shutting down...")

        countdown = 10

        while countdown >= 1:
            print(countdown)
            countdown = countdown - 1

        print("System offline.")
        break

    else:
        print("Invalid choice. Please select 1-4.")