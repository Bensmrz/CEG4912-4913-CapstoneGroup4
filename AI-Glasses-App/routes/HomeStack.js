import { createStackNavigator } from 'react-navigation-stack';
import { createAppContainer } from 'react-navigation';
import ChatLogs from '../pages/ChatLogs';
import Register from '../pages/Register';
import SettingsScreen from '../pages/SettingsScreen';

const screens = {
    ChatLogs: {
        screen: ChatLogs
    },
    Register: {
        screen: Register
    },
    SettingsScreen: {
        screen: SettingsScreen
    },
}

const HomeStack = createStackNavigator(screens);

export default createAppContainer(HomeStack);