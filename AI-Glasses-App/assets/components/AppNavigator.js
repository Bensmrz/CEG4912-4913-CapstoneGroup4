import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator  } from '@react-navigation/native-stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
// import { createDrawerNavigator } from '@react-navigation/drawer';
// import { createStackNavigator } from '@react-navigation/stack';

// Import your screens
import LoginScreen from '../../pages/LoginScreen';
import LoadingScreen from '../../pages/LoadingScreen';
import ChatLogsScreen from '../../pages/ChatLogsScreen';
import RegisterScreen from '../../pages/RegisterScreen';

const Stack = createNativeStackNavigator();
// const Drawer = createDrawerNavigator();

function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="LoginScreen">
        <Stack.Screen name="LoadingScreen" component={LoadingScreen} />
        <Stack.Screen name="LoginScreen" component={LoginScreen} />
        <Stack.Screen name="ChatLogsScreen" component={ChatLogsScreen} />
        <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default AppNavigator;
