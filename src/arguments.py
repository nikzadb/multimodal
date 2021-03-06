import argparse

parser = argparse.ArgumentParser(description='Run commands')

parser.add_argument('-w', '--num-workers', default=1, type=int,
                    help='Number of workers')

parser.add_argument('--sensorpb', default='models/production/tb_models/multimodal_sns_0_611429-0_71.pb', type=str,
                    help='Protobuff File for the Sensor Network')

parser.add_argument('--visionpb', default='models/production/tb_models/multimodal_inception_010-0_860811-0_79.pb', type=str,
                    help='Protobuff File for the Vision Network')

parser.add_argument('--dataset', default='splits/train', type=str,
                    help='Dataset path')

parser.add_argument('--dttype', default='multimodal', type=str,
                    help='Dataset Type')

parser.add_argument('-l', '--log-dir', type=str, default='/tmp/pong',
                    help='Log directory path')
parser.add_argument('-n', '--dry-run', action='store_true',
                    help='Print out commands rather than executing them')
parser.add_argument('-m', '--mode', type=str, default='tmux',
                    help='tmux: run workers in a tmux session. nohup: run '
                         'workers with nohup. child: run workers as child '
                         'processes')
parser.add_argument('-r', '--remotes', default=None,
                    help='The address of pre-existing VNC servers and '
                         'rewarders to use (e.g. -r vnc://localhost:5900'
                         '+15900,vnc://localhost:5901+15901).')
# Add visualise tag
parser.add_argument('--visualise', action='store_true',
                    help='Visualise the gym environment by running '
                         'env.render() between each timestep')

parser.add_argument('-v', '--verbose', action='count', dest='verbosity',
                    default=0, help='Set verbosity.')
parser.add_argument("--evaluate", action="store_true")
parser.add_argument('--task', default=0, type=int, help='Task index')
parser.add_argument('--job-name', default="worker", help='worker or ps')
parser.add_argument('--alpha', default=0.0, help="alpha reward for camera", type=float)
parser.add_argument('--tbport', default=12345, help="Port that tensorboard runs")
args = parser.parse_args()
