# website-capture-monitoring
must install webkit2png first.<br>
webkit2png Install Link : https://github.com/adamn/python-webkit2png

must install line.<br>
line Install Link : http://carpedm20.github.io/line/index.html
fix line api.py
''
        self.transport    = THttpClient.THttpClient(self.LINE_HTTP_URL)
        self.transport_in = THttpClient.THttpClient(self.LINE_HTTP_IN_URL)

        self.transport.setCustomHeaders(self._headers)
        self.transport_in.setCustomHeaders(self._headers)

        self.protocol    = TCompactProtocol.TCompactProtocol(self.transport)
        self.protocol_in = TCompactProtocol.TCompactProtocol(self.transport_in)

        self._client    = CurveThrift.Client(self.protocol)
        self._client_in = CurveThrift.Client(self.protocol_in)

        self.transport.open()
        self.transport_in.open()
