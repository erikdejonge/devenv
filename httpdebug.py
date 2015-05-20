# coding=utf-8
"""
Show connection variables from curl

Usage:
  httpdebug.py [options] <url> [--outfile]

Options:
  -h --help      Show this screen.
  --outfile=<of> File for received data [default: /dev/null].
author  : rabshakeh (erik@a8.nl)
project : devenv
created : 19-05-15 / 16:41
"""
from arguments import Arguments
from cmdssh import call_command
from consoleprinter import colorize_for_print, remove_extra_indentation, clear_screen


def main():
    """
    main
    """
    clear_screen()
    arguments = Arguments(__doc__)
    print(arguments.for_print())
    return
    # noinspection PyUnresolvedReferences
    command = "/usr/bin/curl -s {} -o /dev/null -w ".format(arguments.url)
    command += """
"          content_type:  %{content_type}
    filename_effective:  %{filename_effective}
          p_entry_path:  %{ftp_entry_path}
             http_code:  %{http_code}
          http_connect:  %{http_connect}
              local_ip:  %{local_ip}
            local_port:  %{local_port}
          num_connects:  %{num_connects}
         num_redirects:  %{num_redirects}
          redirect_url:  %{redirect_url}
             remote_ip:  %{remote_ip}
           remote_port:  %{remote_port}
         size_download:  %{size_download}
           size_header:  %{size_header}
          size_request:  %{size_request}
           size_upload:  %{size_upload}
        speed_download:  %{speed_download}
          speed_upload:  %{speed_upload}
     ssl_verify_result:  %{ssl_verify_result}
       time_appconnect:  %{time_appconnect}
          time_connect:  %{time_connect}
       time_namelookup:  %{time_namelookup}
      time_pretransfer:  %{time_pretransfer}
         time_redirect:  %{time_redirect}
    time_starttransfer:  %{time_starttransfer}
            time_total:  %{time_total}
         url_effective:  %{url_effective}
                    ----------

            time_total:  %{time_total}\n"; """.strip()

    result = call_command(command, streamoutput=False, returnoutput=True, ret_and_code=True)

    if result[0] == 0:
        print(colorize_for_print(remove_extra_indentation(result[1], frontspacer="@$", padding=1)).replace("@$", " "))

        # print({1:result[1]})
    else:
        print("error")
        print(result[1])
if __name__ == "__main__":
    main()
