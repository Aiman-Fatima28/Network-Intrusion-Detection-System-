from pythonping import ping
hostaddress = input("Enter single IP or Hostname: ")
while True:
    try:
        result = ping(
            hostaddress,
            count=10000,
            size=1000,
            timeout=1
        )
        print(result)
    except KeyboardInterrupt:
        print("\n ping flood stopped by user.")
        break

    except Exception as e:
        print(f" \n Error: {e}")
        break
    input("\n press enter to continue....")