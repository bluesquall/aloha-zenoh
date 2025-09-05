import zenoh, time

def listener(sample):
    print(f"received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')")

if __name__ == "__main__":
    with zenoh.open(zenoh.Config()) as session:
        key = 'myhome/kitchen/temp'
        sub = session.declare_subscriber(key, listener)
        time.sleep(60)
