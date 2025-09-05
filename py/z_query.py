import zenoh

if __name__ == "__main__":
    with zenoh.open(zenoh.Config()) as session:
        key = 'myhome/kitchen/temp'
        replies = session.get(key)
        for reply in replies:
            try:
                print("Received ('{}': '{}')"
                      .format(reply.ok.key_expr, reply.ok.payload.to_string()))
            except:
                print("Received (ERROR: '{}')"
                      .format(reply.err.payload.to_string()))
