# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set residual control convergance values

    Args:
        _p_: Residual control valeus for p (default: 1e-5)
        _U_: Residual control valeus for U (default: 1e-5)
        _k_: Residual control valeus for k (default: 1e-5)
        _epsilon_: Residual control valeus for epsilon (default: 1e-5)
    Returns:
        residualControl: Butterfly ResidualControl.
"""

ghenv.Component.Name = "Butterfly_residualControl"
ghenv.Component.NickName = "residualControl"
ghenv.Component.Message = 'VER 0.0.01\nJUL_14_2016'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "06::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

#import butterfly
#reload(butterfly)
#reload(butterfly.foamfile)
#reload(butterfly.fvSolution)
from butterfly.fvSolution import ResidualControl

rc = ResidualControl()

if _p_ is not None:
    rc.p = str(_p_)

if _U_ is not None:
    rc.U = str(_U_)

if _k_ is not None:
    rc.k = str(_k_)

if _epsilon_ is not None:
    rc.epsilon = str(_epsilon_)

residualControl = rc