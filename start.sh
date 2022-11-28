if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MOVIESWORLDBoy/DQ-the-file-donor.git /DQ-the-file-donor
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DQ-the-file-donor
fi
cd /DQ-the-file-donor
pip3 install -U -r requirements.txt
echo "Starting ROLEX...."
python3 bot.py
