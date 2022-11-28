if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MOVIESWORLDBoy/DQ-the-file-donor/tree/Private.git /DQ-the-file-donor/tree/Private
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DQ-the-file-donor/tree/Private
fi
cd /DQ-the-file-donor/tree/Private
pip3 install -U -r requirements.txt
echo "Starting ROLEX...."
python3 bot.py
