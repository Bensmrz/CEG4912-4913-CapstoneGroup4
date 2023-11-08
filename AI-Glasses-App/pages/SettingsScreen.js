import React, { useState } from 'react';
import { View, Text, Switch, TextInput, Button } from 'react-native';

function SettingsScreen() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('English');
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 20, marginBottom: 16 }}>Settings</Text>

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Theme</Text>
      <Switch
        value={isDarkMode}
        onValueChange={(value) => setIsDarkMode(value)}
      />

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Language</Text>
      <TextInput
        style={{ borderWidth: 1, padding: 8, marginBottom: 16 }}
        value={selectedLanguage}
        onChangeText={(text) => setSelectedLanguage(text)}
      />

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Change Password</Text>
      <TextInput
        style={{ borderWidth: 1, padding: 8, marginBottom: 8 }}
        placeholder="Current Password"
        value={currentPassword}
        onChangeText={(text) => setCurrentPassword(text)}
        secureTextEntry
      />
      <TextInput
        style={{ borderWidth: 1, padding: 8, marginBottom: 16 }}
        placeholder="New Password"
        value={newPassword}
        onChangeText={(text) => setNewPassword(text)}
        secureTextEntry
      />

<Button
  title="Change Password"
  onPress={() => {
    
    if (currentPassword === '' || newPassword === '') {
      /
      console.log('Please fill in both current and new passwords.');
    } else {
      
    }
  }}
/>


      <Text style={{ fontSize: 16, marginBottom: 8 }}>Notifications</Text>
      <Switch
        value={notificationsEnabled}
        onValueChange={(value) => setNotificationsEnabled(value)}
      />
    </View>
  );
}

export default SettingsScreen;
