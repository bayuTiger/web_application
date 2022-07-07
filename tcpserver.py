import socket


class TCPServer:
    """
    TCP通信を行うサーバーを表すクラス
    """
    def serve(self):
        """
        サーバーを起動する
        """

        print("=== サーバーを起動します ===")

        try:
            # socketを生成
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # socketをlocalhostのポート8080番に割り当てる
            server_socket.bind(("localhost", 8080))
            server_socket.listen(10) # 幾つのクライアントと同時に通信を行えるか

            # 外部からの接続を待ち、接続があったらコネクションを確立する
            print("=== クライアントからの接続を待ちます ===")
            (client_socket, address) = server_socket.accept() # accept()によって、クライアントから新しく接続要求が来るまでプログラムが一時停止する: blockメソッド
            print(f"=== クライアントとの接続が完了しました remote_address: {address} ===")

            # クライアントから送られてきたデータをbytes型で取得する
            request = client_socket.recv(4096) # arg intはネットワークバッファから一回で取得するデータのバイト数: block

            # クライアントから送られてきたデータをファイルに書き出す
            with open("server_recv.txt", "wb") as f:
                f.write(request)

            # 返事は特に返さず、通信を終了させる
            client_socket.close()

        finally:
            print("=== サーバーを停止します。 ===")


if __name__ == '__main__':
    server = TCPServer()
    server.serve()
