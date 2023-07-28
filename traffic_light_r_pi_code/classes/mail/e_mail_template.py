class htmlClass:

    def build_html_code_message(self, message):
        return f"""\
            <tr>
                <td align="center">
                    <p>
                        Raspberry PI Traffic Light Has Sent You A Message.
                        <br>Message Below:
                    </p>
                        <hr>
                        <br>
                        <p>
                            {message}
                        </p>
                </td>
            </tr>
        """

def build_html(heading, body_content):

    return f"""\
    <!DOCTYPE html>
    <html>
        <body style="margin:0;padding:0;">
            <br>
            <table style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                <tr>
                    <td align="center" style="padding:0;">
                        <table style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                            <tr>
                                <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;;">
                                    <img src="cid:image1" alt="" style="height:auto; width: 200px;" />
                                    <h1 style="color: white;">{heading}</h1>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding:36px 30px 42px 30px;">
                                    <table style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                        {body_content}
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
    </html>
    """