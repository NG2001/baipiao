import time

def main():
  try:
    while True:
      print("保持专注，始终前行...")
      time.sleep(1)  # 暂停1秒钟
  except KeyboardInterrupt:
    print("\n专注结束，感谢使用！")

if __name__ == "__main__":
  main()
